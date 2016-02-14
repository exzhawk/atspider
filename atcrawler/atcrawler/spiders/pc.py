# -*- encoding: utf-8 -*-
# Author: Epix
import json

from scrapy import Spider, Request

from atcrawler.items import PCcrawlerItem
from ..info import *


class PC(Spider):
    name = 'pc'
    start_urls = []
    cat = 30

    def start_requests(self):
        for page_num in range(1, PC_MAX_PAGE + 1):
            url = PC_CAT_URL % (self.cat, page_num)
            yield Request(url, callback=self.parse_cat)

    def parse_cat(self, response):
        j = json.loads(response.body)
        for comic in j:
            url = PC_COMICS_URL % comic['id']
            yield Request(url, callback=self.parse_comic)

    def parse_comic(self, response):
        j = json.loads(response.body)
        comic_id = j['comic']['id']
        comic_name = j['comic']['name']
        for ep_num in range(1, int(j['ep_count']) + 1):
            url = PC_EP_URL % (comic_id, ep_num)
            yield Request(url, meta={'name': comic_name}, callback=self.parse_ep)

    def parse_ep(self, response):
        meta = response.meta
        comic_name = self.filter_path(meta['name'])
        j = json.loads(response.body)
        for pic in j:
            try:
                pic_url = pic['url']
                save_path = '/'.join([comic_name] + pic_url.split('/')[-2:])
                json_req = {'jsonrpc': '2.0',
                            'method': 'aria2.addUri',
                            'id': '233',
                            'params': [[pic_url], {'out': save_path}]}
                item = PCcrawlerItem()
                item['req_json'] = json.dumps(json_req)
                yield item
            except:
                print(pic)
                # yield Request(ARIA_URL, method="POST", body=json.dumps(json_req), callback=self.parse_aria)

    @staticmethod
    def filter_path(path):
        return (''.join([i for i in path if i not in r"/\\:*?\"<>|"])).strip()

    def parse_aria(self, response):
        pass
