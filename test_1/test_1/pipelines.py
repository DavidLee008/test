# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: http://doc.scrapy.org/en/latest/topics/item-pipeline.html
import json
import codecs
import sys

reload(sys)
sys.setdefaultencoding('utf8')

class Test1Pipeline(object):
    def __init__(self):
        self.file = codecs.open('test.json',mode='wb',encoding='utf-8')

    def process_item(self, item, spider):
        print "............................"
        #self.file.write('.....................')
        line =json.dumps(dict(item),ensure_ascii=False) + '\r\n'
        self.file.write(line)
        return item

    def spider_closed(self, spider):
        self.file.close()