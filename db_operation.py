#!/usr/bin/python3
import pymongo
from pymongo import MongoClient
from bson.objectid import ObjectId
from bson.json_util import dumps


class DbOperation():
    def __init__(self, dbName):
        client = MongoClient('localhost', 27017)
        self.dbName = dbName
        self.db = client[self.dbName]
        # self.db.drop_collection('profiles')
        

    def getCollection(self, collection):
        if collection in self.db.collection_names(include_system_collections=False):
            return self.db[collection]
        else:
            c = self.db.create_collection(collection)
            c.create_index([('username', pymongo.ASCENDING)], unique=True)
            return c

    def dbInsert(self, article, collection):
        articles = self.getCollection(collection)
        try:
            return articles.insert_one(article).inserted_id
        except:
            return None
        

    def dbFindById(self, id, collection):
        collection = self.getCollection(collection)
        item = collection.find_one({"_id": ObjectId(id)})
        item['_id'] = str(item['_id'])
        return item


    #~~ Articles ~~#
    def dbFindByCategory(self, category):
        collection = self.getCollection('articles')
        articles = list(collection.find({"categoryPredicted": category}).sort("publishedAt", -1))
        new_articles = []
        for article in articles:
            article['_id'] = str(article['_id'])
            new_articles.append(article)
        return new_articles
    #~~~~~~~~~~~~~~#
    
    #~~ Profiles ~~#
    def dbFindProfileByUsername(self, username, json=True):
        collection = self.getCollection('profiles')
        profile = collection.find_one({"username": username})
        if json:
            profile['_id'] = str(profile['_id'])
        return profile

    def dbUpdateProfile(self, newProfile):
        print("Hey", newProfile)
        username = newProfile['username']
        profile = self.dbFindProfileByUsername(username)
        try:
            self.db.profiles.update_one({'username':username}, {"$set": newProfile}, upsert=False)
            return profile['_id']
        except:
            return None

    #~~~~~~~~~~~~~~#




if __name__ == '__main__':
    db = DbOperation('newsapp')
    collection = db.getCollection('articles')
    # profile = db.dbFindProfileByUsername('Saïd', False)
    # print(profile)
    # print()
    for article in collection.find():
         print(article)
    # profile['sources'] = ['espn', 'abc-news', 'bbc-news', 'al-jazeera-news']
    # print(db.dbUpdateProfile("Saïd", profile))


    # print(collection.find_one({"_id": ObjectId('5af963201d41c81e212fbf1d')}))
    # print(ObjectId("5af967141d41c82971e8a695").generation_time)
    # results = db.dbFindByCategory('sports')
    # print(results[0]['url'])
