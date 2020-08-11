from scrapy import cmdline
from sqlobject import sqlhub,connectionForURI
from hrspiders.utils.confighelper import getConfig




cmdline.execute(['scrapy', 'crawl', 'qianchengspider'])