#!/usr/bin/python3


class UserProfile():
    def __init__(self, username=None, password=None, categories=None, sources=None):
        self.username = username
        self.password = password
        self.categories = categories 
        self.sources = sources


    def getUserProfile(self):
        return {
            'username' : self.username,
            'password' : self.password,
            'categories' : self.categories, 
            'sources' : self.sources
        }
               