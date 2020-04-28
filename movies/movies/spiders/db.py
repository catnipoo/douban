# -*- coding: utf-8 -*-
import scrapy
from scrapy.linkextractors import LinkExtractor
from scrapy.spiders import CrawlSpider, Rule


class DbSpider(CrawlSpider):
    name = 'db'
    allowed_domains = ['douban.com']
    start_urls = ['https://movie.douban.com/top250']

    rules = (
        Rule(LinkExtractor(allow=r'https://movie.douban.com/subject/1292052/'), callback='parse_item', follow=True),
    )

    def parse_item(self, response):
        item = {}
        #item['domain_id'] = response.xpath('//input[@id="sid"]/@value').get()
        #item['name'] = response.xpath('//div[@id="name"]').get()
        #item['description'] = response.xpath('//div[@id="description"]').get()
        return item
