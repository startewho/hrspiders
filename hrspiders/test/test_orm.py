

from scrapy import cmdline


from ..service import AreaServer

areaList=AreaServer.getList('')
for a in areaList:
    print('区域id:{},区域名称:{}'.format(a.id,a.name))
