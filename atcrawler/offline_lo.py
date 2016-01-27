# -*- encoding: utf-8 -*-
# Author: Epix
import codecs
import json

from atcrawler.info import *

filename = LO_OFFLINE_FILE
j = json.load(open(filename, 'r'))
l = j['list']
with codecs.open('pic_list.txt', 'w', 'utf8') as output_file:
    for i in l:
        url = LO_URL_PREFIX + i['name'] + '\n'
        output_file.write(url)
