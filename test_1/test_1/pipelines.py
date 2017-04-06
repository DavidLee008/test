# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: http://doc.scrapy.org/en/latest/topics/item-pipeline.html
import json
import codecs
import sys
import MySQLdb
from twisted.enterprise import adbapi
import MySQLdb.cursors
from scrapy.crawler import Settings

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

class MySQLTest1Pipeline(object):
    def __init__(self):
        dbargs = dict(
             host = 'localhost' ,
             db = 'testdb',
             user = 'root', #replace with you user name
             passwd = '123456', # replace with you password
             charset = 'utf8',
             cursorclass = MySQLdb.cursors.DictCursor,
             use_unicode = True,
             )
        self.dbpool = adbapi.ConnectionPool('MySQLdb',**dbargs)

    def process_item(self, item,spider):
        res = self.dbpool.runInteraction(self.insert_into_table,item)
        return item

    def insert_into_table(self,conn,item):
        for i in range(len(item['link'])+1):
            conn.execute('insert into testinfo(id,title,link) values(%s,%s,%s)',
                     (i,item['title'][i-1],item['link'][i-1]))