from ..model.area import Area
from sqlobject import SQLObject,ForeignKey,StringCol,IntCol
from ..bll import Session
class AreaServer:

    @staticmethod
    def getList(query):
        areaSession=Session()
        list=areaSession.query(Area).order_by(Area.id)
        return list