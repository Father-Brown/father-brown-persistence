import py2neo
from py2neo import Graph, NodeSelector
from database.model.Model import Site
from database.model.Model import News
from database.model.Model import Autor
from database.model.Model import Tipo

class NewsResources:

    def __init__(self, graph):       
        self.graph = graph
        self.selector = NodeSelector(graph)

    def get_all_news_from(self, site):
        all_types=self.graph.run('MATCH (s:Site)-[:PUBLICOU]-(n:News), (n)-[:E]-(t:Tipo), (n)-[:POR]-(a:Autor) WHERE s.name="'+site+'" RETURN s,n,t,a limit 25').data()
        dataSet=list()
        for n in all_types:
            dataSet.append(
                {
                    "site":n['s']['url'],
                    "title":n['n']['title'],
                    "subTitle":n['n']['subTitle'],
                    "url":n['n']['url'],
                    "datePublished":n['n']['datePublished'],
                    "content":n['n']['content'],
                    "target":n['t']['description']
                })

        return dataSet


    def get_all_news_from_no_class(self, site):
        all_types=self.graph.run('MATCH (s:Site)-[:PUBLICOU]-(n:News) WHERE s.name="'+site+'" RETURN n').data()
        dataSet=list()
        for n in all_types:
            dataSet.append((n['n']['title'], n['n']['content']), '')

        return dataSet

    def get_news_by_url(self, url):        
        return  News.select(self.graph).where(url=url).first()

    def get_news_by_title(self, title):
        all_types=self.graph.run('MATCH (s:Site)-[:PUBLICOU]-(n:News) WHERE n.title="'+title+'" RETURN n').data()
        news = News()
        for n in all_types:
            news.title=n['n']['title']
            news.url=news.title=n['n']['url']
        return news

    def get_all_data_set(self, sites):
        dataSet = list()
        for s in sites:
            dataSet.extend(self.get_all_news_from(s))
        return dataSet



    def get_all_types(self):
        all_types=self.graph.run('MATCH (t:Tipo) RETURN t').data()
        # dataSet=list()
        # for n in all_types:
        #     dataSet.append((n['description']), '')

        return all_types

    def get_clazz(self, name):
        return Tipo.select(self.graph).where(description=name).first()

    def save_news(self, site, url, title, subTitle, content, autor_name, datePublished, tipo, fonte):
        autor = self.save_autor(autor_name)

        t = self.get_clazz(tipo)
        news =News()
        news.site.add(site)
        news.autor.add(autor)
        news.tipo.add(t)
        news.title=title
        news.subTitle=subTitle
        news.datePublished = datePublished
        news.content=content
        news.url=url
        if fonte is not None:
            news.fonte.add(fonte)
        self.graph.create(news)
        return news

    def classify_news(self,news):
        tx = self.graph.begin()
        self.graph.push(news)
        tx.commit()

    def save_autor(self, name):
        autor = Autor()
        autor.name=name        
        self.graph.push(autor)
        return autor