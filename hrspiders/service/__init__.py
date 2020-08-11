# This package will contain the spiders of your Scrapy project
#
# Please refer to the documentation for information on how to create and manage
# your spiders.



from sqlalchemy.orm import sessionmaker
from sqlalchemy import create_engine
from ..utils.confighelper import getConfig
# configure Session class with desired options
Session = sessionmaker()

constr=getConfig('dbconfig','connetstr')

# later, we create the engine
engine = create_engine(constr)

# associate it with our custom Session class
Session.configure(bind=engine)

from .jobservice import JobService 
from .areaservice import AreaService
