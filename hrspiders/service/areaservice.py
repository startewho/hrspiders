
from ..model import Area
from ..service import Session
class AreaService:

    @staticmethod
    def getList(query):
        areaSession=Session()
        list=areaSession.query(Area).order_by(Area.id)
        return list