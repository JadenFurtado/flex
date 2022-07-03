import pymongo

class MyDatabase:
    def __init__():
        myclient = pymongo.MongoClient("mongodb://localhost:27017/")
        mydb = myclient['requests']
        mycol = mydb['raw_requests']
    
    def insertSchema(self,schema):
        x = self.mycol.insert_one(schema)
        return x
    def displaySchema(self):
        print(self.mycol)