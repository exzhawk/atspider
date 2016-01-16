# -*- encoding: utf-8 -*-
# Author: Epix
import codecs
import json
import os

from lxml import etree

from atcrawler.info import *

dir_path = JD_OFFLINE_FOLDER
files = os.listdir(dir_path)
output_file = codecs.open('pic_list.txt', 'w', 'utf8')
for f in files:
    j = json.load(file(os.path.join(dir_path, f), 'rb'))
    posts = j.get('posts')
    for post in posts:
        content = post.get('content', '')
        tree = etree.HTML(content)
        imgs = tree.xpath('//img/@src')
        for img in imgs:
            output_file.write(unicode(img) + '\n')
