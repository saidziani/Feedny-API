#!/usr/bin/python3


class UserProfile():
    def __init__(self, id=None, username=None, categories=None, sources=None):
        self.id = id 
        self.username = username
        self.categories = categories 
        self.sources = sources


    def getNewsArticle(self):
        return {
            'id' : self.id, 
            'username' : self.username,
            'categories' : self.categories, 
            'sources' : self.sources
        }
               