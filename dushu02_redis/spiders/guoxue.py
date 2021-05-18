# -*- coding: utf-8 -*-
import uuid

import scrapy
from scrapy_redis.spiders import RedisSpider
from scrapy.http import Request
from dushu02_redis.items import Dushu02RedisItem
from scrapy.spiders import crawl, Rule
from scrapy.linkextractors import LinkExtractor

class GuoxueSpider(RedisSpider):
    name = 'guoxue'
    # allowed_domains = ['dushu.com']
    # start_urls = ['http://dushu.com/']
    redis_key = 'gx_start_urls'
    # link = LinkExtractor(allow=r'\d+\.html')
    # link_item = LinkExtractor(allow=r'\d+_\d+\.html')
    # rules = {
    #     Rule(link, callback='parse', follow=True),
    #     Rule(link_item, callback='parse_item', follow=True)
    # }

    def parse(self, response):
        print('-----> 第一级别url:', response.url)
        dl_lists = response.xpath('/html/body/div[5]/div/div[1]/div[1]/dl')
        # '/html/body/div[5]/div/div[1]/div[1]/dl[2]'
        for dl in dl_lists:
            href = dl.xpath('./dt/a/@href').extract_first()
            new_url = 'https://www.dushu.com' + href
            print('-----> 新的url是', new_url)
            yield scrapy.Request(url=new_url, callback=self.parse_item)

    def parse_item(self, response):
        print('-----> 来自于：', response.url)
        li_lists = response.xpath('/html/body/div[6]/div/div[2]/div[2]/ul/li')
        # '/html/body/div[6]/div/div[2]/div[2]/ul/li[13]'
        # '/html/body/div[6]/div/div[1]/div[1]/dl[1]/dd/a/@href'
        for li in li_lists:
            # item = Dushu02RedisItem()
            item = {}
            detail_url = li.xpath('./div/div/a/@href').extract_first()
            name = li.xpath('./div/div/a/img/@alt').extract_first()
            cover = li.xpath('./div/div/a/img/@src').extract_first()
            item['id'] = uuid.uuid4().hex
            item['name'] = name
            item['cover'] = cover
            item['detail_url'] = 'https://www.dushu.com' + detail_url
            print('-----> 数据', detail_url, name, cover)
            yield item
        urls = response.xpath('/html/body/div[6]/div/div[2]/div[3]/div/a/@href').extract()
        for single_url in urls:
            page_url = 'https://www.dushu.com' + single_url
            print('-----> single_url 是：', page_url)
            yield scrapy.Request(url=page_url, callback=self.parse_item)
