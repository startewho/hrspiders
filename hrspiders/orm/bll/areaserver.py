from ..model.area import Area
from sqlobject import SQLObject,ForeignKey,StringCol,IntCol

class AreaServer:

    @staticmethod
    def getList(query):
        list=Area.select(Area.q.id>1000)
        return list