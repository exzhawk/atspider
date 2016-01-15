# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: http://doc.scrapy.org/en/latest/topics/item-pipeline.html
import scrapy.pipelines.files


class AtcrawlerPipeline(scrapy.pipelines.files.FilesPipeline):
    def process_item(self, item, spider):
        return item
