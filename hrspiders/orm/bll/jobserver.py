from ..model import Job
from sqlobject import SQLObject,ForeignKey,StringCol,IntCol
from ..bll import Session
class JobServer:

    @staticmethod
    def getList(query):
        areaSession=Session()
        list=areaSession.query(Job).order_by(Job.url)
        return list