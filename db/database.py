from peewee import *

#-----------------------------------------------CREATE MODEL AND CONNECT TO THE DB----------------------------------------------
# Connect to the database with the db class
db = PostgresqlDatabase('realstatenyc', user='rodrigow', password='Rod99', host='localhost', port=5432)

# Define the base model
class BaseModel(Model):
  class Meta:
    database = db

# Create a model to the database
class Apartments(BaseModel):
  latitude = FloatField()
  longitude = FloatField()
  floorSize = IntegerField()
  url = CharField()
  price = FloatField()

# Connect to database
db.connect()
# # Drop the database if you run again
# db.drop_tables([Apartments])
# # Create the tables
# db.create_tables([Apartments])
  
