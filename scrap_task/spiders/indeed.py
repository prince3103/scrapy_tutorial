# -*- coding: utf-8 -*-
import scrapy
from scrapy.linkextractors import LinkExtractor
from scrapy.spiders import CrawlSpider, Rule


class IndeedSpider(CrawlSpider):
    name = 'indeed'
    allowed_domains = ['flipkart.com']
    
    def start_requests(self):
        yield scrapy.Request(url='https://www.flipkart.com/televisions/pr?sid=ckf,czl&q=telivision&otracker=categorytree')

    rules = (
        Rule(LinkExtractor(restrict_xpaths='//div[@class="_1UoZlX"]/a'), callback='parse_item', follow=True),
        Rule(LinkExtractor(restrict_xpaths="(//a[@class='lister-page-nextnext-page'])[2]"))
    )



    def parse_item(self, response):
        yield {
            'title': response.xpath("//span[@class='_35KyD6']/text()").get(),
            'price': response.xpath("//div[@class='_1vC4OE _3qQ9m1']/text()").get(),
            'user-agent': response.request.headers.get('User-Agent').decode('utf-8'),
            'proxy': response.meta.get('proxy')
        }