# -*- coding: utf-8 -*-
import re

import scrapy
from scrapy.linkextractors import LinkExtractor
from scrapy.spiders import CrawlSpider, Rule
from ..items import MoviesItem

class DbSpider(CrawlSpider):
    name = 'db'
    allowed_domains = ['douban.com']
    start_urls = ['https://movie.douban.com/top250']

    rules = (
        Rule(LinkExtractor(allow=r'https://movie.douban.com/subject/\d+/'), callback='parse_item'),
        Rule(LinkExtractor(allow=r'\?start=\d+&filter='), follow=True),
    )

    def parse_item(self, response):
        item = MoviesItem()
        item['title'] = response.xpath("//span[@property='v:itemreviewed']/text()").extract_first()
        item['director'] = response.xpath("//a[@rel='v:directedBy']/text()").extract_first()
        item['screenwriter'] =' / '.join(response.xpath("//span[text()='编剧']/../span[2]/a/text()").extract())
        item['starring'] = ' / '.join(response.xpath("//span[@class='actor']/span[2]/a/text()").extract())
        item['types'] = ' / '.join(response.xpath("//span[@property='v:genre']/text()").extract())
        item['area'] = re.findall(r'<span class="pl">制片国家/地区:</span> (.*?)<br/>',response.body.decode())[0]
        item['language'] = re.findall(r'<span class="pl">语言:</span> (.*?)<br/>',response.body.decode())[0]
        item['date'] = ' / '.join(response.xpath("//span[@property='v:initialReleaseDate']/text()").extract())
        item['lengh'] = response.xpath("//span[@property='v:runtime']/text()").extract_first()
        item['aka'] = re.findall(r'<span class="pl">又名:</span> (.*?)<br/>',response.body.decode())[0]
        item['imdb_href'] = re.findall(r'IMDb链接:</span> <a href="(.*?)" target="_blank" rel="nofollow">',response.body.decode())[0]
        item['img_url'] = response.xpath("//img[@rel='v:image']/@src").extract_first()
        item['score'] = response.xpath("//strong/text()").extract_first()
        item['score'] = float(item['score'])
        item['synopsis'] = response.xpath("//span[@class='all hidden']/text()").extract_first()
        if item['synopsis'] is None:
            item['synopsis'] = response.xpath("//span[@property='v:summary']/text()").extract_first()
        item['synopsis'] = re.sub('\\n','',item['synopsis'])
        item['synopsis'] = re.sub('\\u3000','',item['synopsis'])
        item['synopsis'] = re.sub('                                ','',item['synopsis'])
        # print('*'*100)
        # print(type(item['synopsis']))
        print(item)
        yield item