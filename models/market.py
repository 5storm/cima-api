from peewee import *

from database import Database
from .region import Region

class Market(Model):
    id = BigAutoField(unique=True)
    name = CharField()
    region_id = ForeignKeyField(Region.id)

    class Meta:
        database = Database.getInstance()
