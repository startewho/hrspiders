from sqlobject import SQLObject,ForeignKey,StringCol,IntCol

class Area(SQLObject):

    class sqlmeta:
        lazyUpdate = True
        cacheValues = False
    id=IntCol()
    areaCode=StringCol()
    areaSimple=StringCol()
    phoneCode=StringCol()
    name=StringCol()
    pid=IntCol()

