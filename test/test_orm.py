from scrapy import cmdline
from sqlobject import sqlhub,connectionForURI

import pymysql

import sys,os
sys.path.append(os.path.dirname(__file__) + os.sep + '../')
from utils.confighelper import getConfig
from hrspiders.orm.bll.areaserver import AreaServer

constr=getConfig('dbconfig','connetstr')
sqlhub.processConnection = connectionForURI(constr)
areaList=AreaServer.getList('')
for a in areaList:
    print('区域id:{},区域名称:{}'.format(a.id,a.name))
