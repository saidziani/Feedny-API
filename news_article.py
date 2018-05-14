#!/usr/bin/python3


class NewsArticle():
    def __init__(self, url=None, author=None, source=None, title=None, content=None, urlToImage=None, publishedAt=None, summaryGenerated=None, categoryPredicted=None):
        self.url = url
        self.title = title
        self.source = source
        self.author = author
        self.content = content
        self.urlToImage = urlToImage
        self.publishedAt = publishedAt
        self.summaryGenerated = summaryGenerated
        self.categoryPredicted = categoryPredicted


    def getNewsArticle(self):
        return {
            'url': self.url,
            'title': self.title,
            'source': self.source,
            'author': self.author,
            'content': self.content,
            'urlToImage': self.urlToImage,
            'publishedAt': self.publishedAt,
            'summaryGenerated': self.summaryGenerated,
            'categoryPredicted': self.categoryPredicted
        }
               