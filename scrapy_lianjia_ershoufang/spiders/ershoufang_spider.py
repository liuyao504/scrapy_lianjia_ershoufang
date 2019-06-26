import scrapy
from scrapy.http.response.text import TextResponse
from datetime import datetime
import hashlib

from scrapy_lianjia_ershoufang.items import ScrapyLianjiaErshoufangItem


class ErshoufangSpider(scrapy.Spider):
    name = 'ErshoufangSpider'

    def __init__(self, name=None, **kwargs):
        super().__init__(name=None, **kwargs)
        if getattr(self, 'city', None) is None:
            setattr(self, 'city', 'sz')
        self.allowed_domains = ['%s.lianjia.com' % getattr(self, 'city')]

    def start_requests(self):
        city = getattr(self, 'city')
        urls = ['https://%s.lianjia.com/ershoufang/pg%d/' % (city, i)
                for i in range(1, 101)]
        for url in urls:
            yield scrapy.Request(url, self.parse, headers={'Referer': url})

    def parse(self, response: TextResponse):
        items = response.css('ul.sellListContent li')
        for li in items:
            item = ScrapyLianjiaErshoufangItem()
            item['title'] = li.css('div.title a::text').get().replace('：', '').replace(',', ' ').replace("\n", '')
            house_infos = li.css('div.address .houseInfo::text').re(
                r'\|\s+(.*)\s+\|\s+(.*)平米\s+\|\s+(.*)\s+\|\s+(.*)\s+\|\s+(.*)')
            item['room'] = house_infos[0]
            item['area'] = house_infos[1]
            item['orientation'] = house_infos[2]
            item['decoration'] = house_infos[3]
            item['elevator'] = house_infos[4]
            item['xiaoqu'] = li.css('div.address a::text').get()
            item['flood'] = li.css('div.flood .positionInfo::text').get().replace('-', '').strip()
            item['location'] = li.css('div.flood .positionInfo a::text').get()
            follow_infos = li.css('div.followInfo::text').re(r'(.*)人关注\s+/\s+共(.*)次带看\s+/\s+(.*)发布')
            item['follow_number'] = follow_infos[0]
            item['look_number'] = follow_infos[1]
            item['pub_duration'] = follow_infos[2]
            item['total_price'] = li.css('div.priceInfo div.totalPrice span::text').get()
            unit_price = li.css('div.priceInfo .unitPrice span::text').re(r'单价(.*)元/平米')
            item['unit_price'] = unit_price[0]
            item['total_unit'] = li.css('div.totalPrice::text').get()
            item['crawl_time'] = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
            item['house_id'] = self.genearteMD5(''.join((str(item['title']), str(item['room']), str(item['area']),
                                                         str(item['orientation']), str(item['elevator']),
                                                         str(item['xiaoqu']),
                                                         str(item['flood']), str(item['location']))))
            yield item

    def genearteMD5(self, text):
        # 创建md5对象
        hl = hashlib.md5()
        hl.update(text.encode(encoding='utf-8'))
        return hl.hexdigest()
