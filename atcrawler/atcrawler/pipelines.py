# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: http://doc.scrapy.org/en/latest/topics/item-pipeline.html
from scrapy.exceptions import DropItem


class AtcrawlerPipeline(object):
    def __init__(self):
        self.file = open('pic_list.txt', 'w')
        self.seen = set()

    def process_item(self, item, spider):
        image_url = item['image_url']
        if image_url in self.seen:
            raise DropItem("Duplicate item found: %s" % item)
        else:
            self.seen.add(image_url)
            line = image_url + '\n'
            self.file.write(line)
            return item
