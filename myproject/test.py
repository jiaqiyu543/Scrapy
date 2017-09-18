import requests,os,pymongo
import random

c=pymongo.MongoClient()
db=c.chemicalbook1
co=db.names
print(co.find().count())

