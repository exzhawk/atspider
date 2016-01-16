# -*- encoding: utf-8 -*-
# Author: Epix
import json

from lxml import etree
from scrapy import Spider

from atcrawler.items import AtcrawlerItem
from ..info import *


class JD(Spider):
    name = 'jd'
    start_urls = [JD_BASE_URL % page_number for page_number in xrange(1, JD_PAGE_MAX + 1)]
    pass

    def make_requests_from_url(self, url):
        r = super(JD, self).make_requests_from_url(url)
        # r.meta['proxies'] = '127.0.0.1:8089'
        return r

    def parse(self, response):
        try:
            j = json.loads(response.body)
            posts = j.get('posts')
            for post in posts:
                content = post.get('content', '')
                tree = etree.HTML(content)
                imgs = tree.xpath('//img/@src')
                for img in imgs:
                    try:
                        item = AtcrawlerItem()
                        item['image_url'] = img
                        yield item
                    except:
                        pass
        except:
            pass
