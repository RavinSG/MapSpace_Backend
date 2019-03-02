from pymongo import MongoClient
import pytz


client = MongoClient('localhost', 27017)

db = client.MapSpace
timezone = pytz.timezone('Asia/Colombo')
