# -*- coding: utf-8 -*-

# Scrapy settings for dushu02_redis project
#
# For simplicity, this file contains only settings considered important or
# commonly used. You can find more settings consulting the documentation:
#
#     https://docs.scrapy.org/en/latest/topics/settings.html
#     https://docs.scrapy.org/en/latest/topics/downloader-middleware.html
#     https://docs.scrapy.org/en/latest/topics/spider-middleware.html
import os

BOT_NAME = 'dushu02_redis'

SPIDER_MODULES = ['dushu02_redis.spiders']
NEWSPIDER_MODULE = 'dushu02_redis.spiders'


# Crawl responsibly by identifying yourself (and your website) on the user-agent
USER_AGENT = 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/86.0.4240.111 Safari/537.36'

# Obey robots.txt rules
ROBOTSTXT_OBEY = False
LOG_LEVEL = 'INFO'
# 指定管道
ITEM_PIPELINES = {
   'dushu02_redis.pipelines.EsPipeline': 300,
}
# ITEM_PIPELINES = {
#    'scrapy_redis.pipelines.RedisPipeline': 400,
#    'dushu02_redis.pipelines.Dushu02RedisPipeline': 300,
# }
# 配置调度器和其他
# 增加了一个去重容器类的配置, 作用使用Redis的set集合来存储请求的指纹数据, 从而实现请求去重的持久化
DUPEFILTER_CLASS = "scrapy_redis.dupefilter.RFPDupeFilter"
# 使用scrapy-redis组件自己的调度器
SCHEDULER = "scrapy_redis.scheduler.Scheduler"
# 配置调度器是否要持久化, 也就是当爬虫结束了, 要不要清空Redis中请求队列和去重指纹的set。如果是True, 就表示要持久化存储, 就不清空数据, 否则清空数据
SCHEDULER_PERSIST = True
#指定redis
# REDIS_HOST = '192.168.99.100' #redis远程服务器的ip（修改）
# REDIS_PORT = 6379
# REDIS_ENCODING = 'utf-8'
# 配置es搜索引擎的HOST
ES_HOST = '192.168.18.158'
ES_PORT = '9200'
ES_INDEX_NAME = 'dushu'
ES_TYPE_NAME = 'guoxue'
# REDIS_PARAMS = {'password': '111111'}
# 或者直接用REDIS_URL搞定
# REDIS_URL = 'redis://[:password@]127.0.0.1:6379/7'
REDIS_URL = 'redis://192.168.18.158:6379/0'
# http://192.168.18.101/
# Configure maximum concurrent requests performed by Scrapy (default: 16)
#CONCURRENT_REQUESTS = 32

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
# 配置日志
LOG_LEVEL = 'INFO'
LOG_FILE = os.path.join(BASE_DIR, 'dushu.log')
LOG_FORMAT = '%(asctime)s - %(levelname)s - %(message)s'
LOG_DATEFORMAT = '%Y/%m/%d %H:%M:%S'


# Configure a delay for requests for the same website (default: 0)
# See https://docs.scrapy.org/en/latest/topics/settings.html#download-delay
# See also autothrottle settings and docs
DOWNLOAD_DELAY = 1
# The download delay setting will honor only one of:
#CONCURRENT_REQUESTS_PER_DOMAIN = 16
#CONCURRENT_REQUESTS_PER_IP = 16

# Disable cookies (enabled by default)
#COOKIES_ENABLED = False

# Disable Telnet Console (enabled by default)
#TELNETCONSOLE_ENABLED = False

# Override the default request headers:
#DEFAULT_REQUEST_HEADERS = {
#   'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8',
#   'Accept-Language': 'en',
#}

# Enable or disable spider middlewares
# See https://docs.scrapy.org/en/latest/topics/spider-middleware.html
#SPIDER_MIDDLEWARES = {
#    'dushu02_redis.middlewares.Dushu02RedisSpiderMiddleware': 543,
#}

# Enable or disable downloader middlewares
# See https://docs.scrapy.org/en/latest/topics/downloader-middleware.html
DOWNLOADER_MIDDLEWARES = {
   'dushu02_redis.middlewares.Dushu02RedisDownloaderMiddleware': 543,
}

# Enable or disable extensions
# See https://docs.scrapy.org/en/latest/topics/extensions.html
#EXTENSIONS = {
#    'scrapy.extensions.telnet.TelnetConsole': None,
#}

# Configure item pipelines
# See https://docs.scrapy.org/en/latest/topics/item-pipeline.html
# ITEM_PIPELINES = {
#    'dushu02_redis.pipelines.Dushu02RedisPipeline': 300,
# }


# Enable and configure the AutoThrottle extension (disabled by default)
# See https://docs.scrapy.org/en/latest/topics/autothrottle.html
#AUTOTHROTTLE_ENABLED = True
# The initial download delay
#AUTOTHROTTLE_START_DELAY = 5
# The maximum download delay to be set in case of high latencies
#AUTOTHROTTLE_MAX_DELAY = 60
# The average number of requests Scrapy should be sending in parallel to
# each remote server
#AUTOTHROTTLE_TARGET_CONCURRENCY = 1.0
# Enable showing throttling stats for every response received:
#AUTOTHROTTLE_DEBUG = False

# Enable and configure HTTP caching (disabled by default)
# See https://docs.scrapy.org/en/latest/topics/downloader-middleware.html#httpcache-middleware-settings
#HTTPCACHE_ENABLED = True
#HTTPCACHE_EXPIRATION_SECS = 0
#HTTPCACHE_DIR = 'httpcache'
#HTTPCACHE_IGNORE_HTTP_CODES = []
#HTTPCACHE_STORAGE = 'scrapy.extensions.httpcache.FilesystemCacheStorage'
