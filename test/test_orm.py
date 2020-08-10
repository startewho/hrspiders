from scrapy import cmdline

import sys,os
sys.path.append("..")
from  utils import confighelper
from  hrspiders.orm.bll.areaserver import AreaServer


areaList=AreaServer.getList('')
for a in areaList:
    print('区域id:{},区域名称:{}'.format(a.id,a.name))
