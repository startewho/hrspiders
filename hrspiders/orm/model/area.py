from sqlobject import SQLObject,ForeignKey,StringCol,IntCol

# 区域表
class Area(SQLObject):

    class sqlmeta:
        idName='id'
        lazyUpdate = True
        cacheValues = False
   
    areaCode=StringCol()
    areaSimple=StringCol()
    phoneCode=StringCol()
    name=StringCol()
    pid=IntCol()

