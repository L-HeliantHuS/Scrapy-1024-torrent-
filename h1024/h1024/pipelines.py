# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://doc.scrapy.org/en/latest/topics/item-pipeline.html

from pymongo import MongoClient

class H1024Pipeline(object):
    def process_item(self, item, spider):
        if spider.name == "h1024p":
            client = MongoClient()['spider']['1024']
            client.insert(item)



