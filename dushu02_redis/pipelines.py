# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html
import time

import requests


class EsPipeline:
    def process_item(self, item, spider):
        doc_id = item.pop('id')

        doc_url = spider.doc_url + f'{doc_id}/'

        requests.post(doc_url, json=item)
        spider.logger.info(f'{item} 成功写入ES')
        time.sleep(0.1)     # 给ES服务器减少一点压力

        return item
