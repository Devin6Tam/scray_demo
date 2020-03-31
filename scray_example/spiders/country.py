# -*- coding: utf-8 -*-
import scrapy
from scrapy.linkextractors import LinkExtractor
from scrapy.spiders import CrawlSpider, Rule
from scray_example.items import ScrayExampleItem

class CountrySpider(CrawlSpider):
    name = 'country'
    allowed_domains = ['example.webscraping.com']
    start_urls = ['http://example.webscraping.com/']

    rules = (
        Rule(LinkExtractor(allow=r'places/default/index/', deny='/user/'), follow=True),
        Rule(LinkExtractor(allow=r'places/default/view/', deny='/user/'), callback='parse_item')
    )

    def parse_item(self, response):
        item = ScrayExampleItem()
        name_css = 'tr#places_country__row td.w2p_fw::text'
        item['name'] = response.css(name_css).extract()
        population_css = 'tr#places_population__row td.w2p_fw::text'
        item['population'] = response.css(population_css).extract()
        return item
