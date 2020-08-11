# -*- coding: utf-8 -*-

import pymysql
from time import strftime
from .service import JobService,Session
from .model import Job
class QianchengwuyouPipeline(object):
    def open_spider(self, spider):
        self.session = Session()
        self.jobService = JobService(self.session)

    def close_spider(self, spider):
        self.session.Remove()


    def process_item(self, item, spider):
        item['collect_date'] = strftime('%Y-%m-%d')
        job=Job()
        for k in item:
         job[k]=item[k]
        return item

