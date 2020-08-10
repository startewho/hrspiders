from configparser import ConfigParser

def getConfig(section,item):
 cfg = ConfigParser()
 cfg.read('..\scrapy.cfg')
 return cfg.get(section,item)