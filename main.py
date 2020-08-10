from scrapy import cmdline
from sqlobject import sqlhub,connectionForURI
from utils.confighelper import getConfig
import pymysql


constr=getConfig('dbconfig','connetstr')
sqlhub.processConnection = connectionForURI(constr)
cmdline.execute(['scrapy', 'crawl', 'qianchengspider'])