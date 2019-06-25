#!/bin/sh

git filter-branch --env-filter '
an="$GIT_AUTHOR_NAME"
am="$GIT_AUTHOR_EMAIL"
cn="$GIT_COMMITTER_NAME"
cm="$GIT_COMMITTER_EMAIL"
if [ "$GIT_COMMITTER_EMAIL" = "guoziwei93@gmail.com" ]
then
    cn="liuyao504"
    cm="liuyao504@gmail.com"
fi
if [ "$GIT_AUTHOR_EMAIL" = "guoziwei93@gmail.com" ]
then
    an="liuyao504"
    am="liuyao504@gmail.com"
fi
    export GIT_AUTHOR_NAME="$an"
    export GIT_AUTHOR_EMAIL="$am"
    export GIT_COMMITTER_NAME="$cn"
    export GIT_COMMITTER_EMAIL="$cm"
'