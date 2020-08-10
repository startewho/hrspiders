from scrapy import cmdline
from sqlobject import sqlhub,connectionForURI
from utils.confighelper import getConfig




cmdline.execute(['scrapy', 'crawl', 'qianchengspider'])