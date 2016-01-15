# -*- encoding: utf-8 -*-
# Author: Epix

import requests
from scrapy import Spider

from atcrawler.items import AtcrawlerItem
from ..info import *
from ..settings import *


class AT(Spider):
    name = 'at'
    start_urls = [BASE_URL.format(**dict([('number', 1), ('type', 1), ('mode', 1)]))]
    session = requests.session()
    session.headers = {'user-agent': USER_AGENT}

    def parse(self, r):
        for type_number in TYPE_RANGE:
            for mode_number in MODE_RANGE:
                start_number = 0
                has_next = True
                while has_next:
                    url = BASE_URL.format(**dict([('number', start_number),
                                                  ('type', type_number),
                                                  ('mode', mode_number)]))
                    response = self.session.get(url)
                    start_number += 50
                    j = response.json()
                    blogs = j.get('data').get('blogs')
                    if blogs:
                        img_srcs = []
                        for blog in blogs:
                            img_src = blog.get('isrc').replace('/images_min/', '/images/')
                            img_srcs.append(img_src)
                        if img_srcs:
                            item = AtcrawlerItem()
                            item['image_urls'] = list(img_srcs)
                            yield item
                    else:
                        has_next = False
