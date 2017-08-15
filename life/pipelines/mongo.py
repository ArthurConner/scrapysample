from datetime import datetime
import txmongo
from scrapy.conf import settings
from twisted.internet import defer, reactor
from twisted.python import log


def getConnection():
	mongodb_uri = "mongodb://" +settings['MONGODB_SERVER'] + ":" + str(settings['MONGODB_PORT'])
	print("getting connection..." + str(mongodb_uri))
	mongo =   txmongo.MongoConnectionPool()
	print("pool :" +str(mongo))
	return mongo


def getDatabase(conn, dbName):
	print("getting database..." + dbName)
	return getattr(conn, dbName)


def getCollection(db, collName):
	print("getting collection..." + collName)
	return getattr(db, collName)


class Mongo(object):
	def __init__(self):
		con = getConnection()
		foo = getDatabase(con,settings['MONGODB_DB'])
		self.collection = getCollection(foo,settings['MONGODB_COLLECTION'])

	def process_item(self, item, spider):
		valid = True
		for data in item:
			if not data:
				valid = False
				raise DropItem("Missing {0}!".format(data))
		if valid:
			self.collection.insert(dict(item), safe=True)
			print(" added to MongoDB database!")
		return item