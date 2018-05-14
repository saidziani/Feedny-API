#!/usr/bin/python3
from newspaper import Article
from newsapi import NewsApiClient
from news_article import NewsArticle
from db_operation import DbOperation

class Helper():
    def __init__(self):
        self.newsapi = NewsApiClient(api_key='401ff7e72a054bf88dd8fffa4af72f96')
        self.dbOperation = DbOperation('newsapp')
        

    def getArticleContent(self, url):
        article = Article(url)
        article.download()
        article.parse()
        return article.text


    def getTopBySources(self, sources):
        # newsapi.get_top_headlines(sources='abc-news, bbc-news, al-jazeera-english')
        sources = ', '.join(sources)
        return self.newsapi.get_top_headlines(sources=sources)


    def getArticles(self, topHeadlines):
        return topHeadlines['articles']


    def setArticleDetails(self, article):
        content = self.getArticleContent(article['url'])
        summaryGenerated = "placeholderSummary"
        categoryPredicted = "placeholderCategory"
        article = NewsArticle(url=article['url'], author=article['author'], source=article['source']['id'], title=article['title'], content=content, urlToImage=article['urlToImage'], publishedAt=article['publishedAt'], summaryGenerated=summaryGenerated, categoryPredicted=categoryPredicted)
        return article


    def getArticlesByCategory(self, category):
        return self.dbOperation.dbFindByCategory(category)


if __name__ == '__main__':
    help = Helper()
    # dbOperation = DbOperation('newsapp')
    # sources = ['espn']
    # topHeadlines = help.getTopBySources(sources)
    # article = help.getArticles(topHeadlines)[0] 
    # article = help.setArticleDetails(article).getNewsArticle()
    # id = dbOperation.dbInsert(article)
    # print(id)

    print(help.getArticlesByCategory('da'))
