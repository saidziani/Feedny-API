#!/usr/bin/python3
from newspaper import Article
from newsapi import NewsApiClient
from news_article import NewsArticle
from db_operation import DbOperation

class ApiHelper():
    def __init__(self):
        self.newsapi = NewsApiClient(api_key='401ff7e72a054bf88dd8fffa4af72f96')
        self.dbOperation = DbOperation('newsapp')
        

    def getArticleContent(self, url):
        article = Article(url)
        try:
            article.download()
        except:
            article = None
        if article != None:
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
        categoryPredicted = self.setCategoryEnglish(content)
        article = NewsArticle(
            url=article['url'], 
            author=article['author'], 
            source=article['source']['id'], 
            title=article['title'], 
            content=content, 
            urlToImage=article['urlToImage'], 
            publishedAt=article['publishedAt'], 
            summaryGenerated=summaryGenerated, 
            categoryPredicted=categoryPredicted
        )
        return article.getNewsArticle()


    def insertArticles(self, sources):
        articles = self.getTopBySources(sources)['articles']
        for article in articles:
            article = self.setArticleDetails(article)
            id = self.dbOperation.dbInsert(article)
            print('OK:', id)    
        return 'DONE FOR ALL ARTICLES.'
      

    def getArticlesByCategory(self, category):
        articles = self.dbOperation.dbFindByCategory(category)
        result = []
        for article in articles:
            result.append(Article)
        return articles

    def getArticleById(self, id):
        return self.dbOperation.dbFindById(id)

    def setCategoryArabic(self, article):
        import sys
        sys.path.insert(0,"../ArabicTextCategorization/lib/")
        from helper import Helper 
        predictHelp = Helper()
        predictedCategory = predictHelp.predict(article)
        return predictedCategory

    def setCategoryEnglish(self, article):
        import sys
        sys.path.insert(0,"../EnglishTextCategorization/")
        from Predict import predict 
        predictedCategory = predict(article)
        return predictedCategory
