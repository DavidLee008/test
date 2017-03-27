# -*- coding:utf-8 -*-
from scrapy.spiders import Spider
from scrapy.selector import Selector
from test_1.items import Test1Item
from scrapy import Request


class test1Spider(Spider):
    name = 'test_1'
    start_urls = [
        'http://www.leiphone.com/'
    ]

    def parse(self, response):
        sel = Selector(response)
        item = Test1Item()
        #urls = sel.xpath('//h3/a/@href').extract()
        #for url in urls:
        #request = Request(url= 'http://www.leiphone.com/', dont_filter=True)
        #request.meta['PhantomJS'] = True
        #print url
        #yield request

        item['title'] = sel.xpath('//h3/a/@title').extract()
        yield item