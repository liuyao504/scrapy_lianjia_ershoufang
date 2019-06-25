# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# https://doc.scrapy.org/en/latest/topics/items.html

import scrapy


class ScrapyLianjiaErshoufangItem(scrapy.Item):
    # define the fields for your item here like:
    title = scrapy.Field()
    room = scrapy.Field()
    area = scrapy.Field()
    orientation = scrapy.Field()
    elevator = scrapy.Field()
    decoration = scrapy.Field()
    location = scrapy.Field()
    xiaoqu = scrapy.Field()
    flood = scrapy.Field()
    follow_number = scrapy.Field()
    look_number = scrapy.Field()
    pub_duration = scrapy.Field()
    total_price = scrapy.Field()
    unit_price = scrapy.Field()
    unit = scrapy.Field()

