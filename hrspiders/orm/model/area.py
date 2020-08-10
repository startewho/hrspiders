from sqlobject import SQLObject,ForeignKey,StringCol,IntCol

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

