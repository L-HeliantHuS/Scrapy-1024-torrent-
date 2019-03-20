from pymongo import MongoClient
import time

while True:
	client = MongoClient()['spider']['1024']
	print(client.count())
	time.sleep(2)