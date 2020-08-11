from ..model import Job
from ..service import Session
class JobService:

    def __init__(self, session):
        self.session = session

    def getList(query):
        list=self.session.query(Job).order_by(Job.url)
        return list

    def addItem(job):
        list=self.session.query(Job).order_by(Job.url)
        return list