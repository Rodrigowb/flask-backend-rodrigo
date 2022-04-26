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
# Drop the database if you run again
db.drop_tables([Apartments])
# Create the tables
db.create_tables([Apartments])

#-----------------------------------------------SEED THE DB MANUALLY----------------------------------------------
Apartments(latitude=40.52, longitude=-74.17, floorSize=4200, url='https://www.zillow.com/homedetails/440-Philip-Ave-Staten-Island-NY-10312/32366837_zpid/', price=1350000).save()
Apartments(latitude=50.24, longitude=-76, floorSize=5000, url='https://www.zillow.com/homedetails/40-Bennett-St-Staten-Island-NY-10302/62723283_zpid/', price=595000).save()
Apartments(latitude=20.45, longitude=10, floorSize=3000, url='https://www.zillow.com/homedetails/1933-Vyse-Ave-Bronx-NY-10460/83178654_zpid/', price=600400).save()

