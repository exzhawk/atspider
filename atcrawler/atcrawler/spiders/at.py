# -*- encoding: utf-8 -*-
# Author: Epix
import json
import urlparse

import requests
from scrapy import Spider, Request

from atcrawler.items import AtcrawlerItem
from ..info import *
from ..settings import *


class AT(Spider):
    name = 'at'
    start_urls = []
    for type_number in TYPE_RANGE:
        for mode_number in MODE_RANGE:
            start_urls.append(BASE_URL.format(**dict([('st', 0), ('type', type_number), ('mode', mode_number)])))
    session = requests.session()
    session.headers = {'user-agent': USER_AGENT}

    def parse(self, response):
        j = json.loads(response.body)
        blogs = j.get('data').get('blogs')
        if blogs:
            img_srcs = []
            for blog in blogs:
                img_src = blog.get('isrc').replace('/images_min/', '/images/')
                img_srcs.append(img_src)
            item = AtcrawlerItem()
            item['image_urls'] = list(img_srcs)
            yield item
            url_component = urlparse.urlparse(response.url)
            q_component = urlparse.parse_qs(url_component.query)
            type_number = q_component.get('type')[0]
            mode_number = q_component.get('mode')[0]
            st_number = int(q_component.get('st')[0])
            st_number += 50
            url = BASE_URL.format(**dict([('st', st_number), ('type', type_number), ('mode', mode_number)]))
            yield Request(url, callback=self.parse)
