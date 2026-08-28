from mongoengine import connect
from config.settings import MONGODB_URI, MONGODB_DB
def connect_database():
    connect(db=MONGODB_DB,host=MONGODB_URI)
