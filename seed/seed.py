from peewee import *
import sys
sys.path.insert(0, "..")
from db.database import Apartments
from db.database import db

class Seed:
  """
  Seed the database using different methods
  """
  def __init__(self):
    pass

  def drop_create(self):
    db.drop_tables([Apartments])
    db.create_tables([Apartments])
    return Apartments
  
  def seed_manually(self):
    """
    Seed the database using sql syntax
    """
    db.create_tables([Apartments])
    Apartments(latitude=40.52, longitude=-74.17, floorSize=4200, url='https://www.zillow.com/homedetails/440-Philip-Ave-Staten-Island-NY-10312/32366837_zpid/', price=1350000).save()
    Apartments(latitude=50.24, longitude=-76, floorSize=5000, url='https://www.zillow.com/homedetails/40-Bennett-St-Staten-Island-NY-10302/62723283_zpid/', price=595000).save()
    Apartments(latitude=20.45, longitude=10, floorSize=3000, url='https://www.zillow.com/homedetails/1933-Vyse-Ave-Bronx-NY-10460/83178654_zpid/', price=600400).save()
    return Apartments


if __name__ == '__main__':
  seed = Seed()
  seed.drop_create()
  seed.seed_manually()

