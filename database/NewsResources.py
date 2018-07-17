import py2neo
from py2neo import Graph
from database.model.Model import Site
from database.model.Model import News
from database.model.Model import Autor
from database.model.Model import Tipo

class NewsResources:

    def __init__(self, graph):       
        self.graph = graph

    def get_all_news_from(self, site):
        # news=set()
        all_types=self.graph.run('MATCH (s:Site)-[:PUBLICOU]-(n:News)-[:E]-(t:Tipo) WHERE s.name="'+site+'" RETURN s,n,t').data()
        dataSet=list()
        for n in all_types:
            dataSet.append(
                {
                    "site":n['s']['url'],
                    "title":n['n']['title'],
                    "url":n['n']['url'],
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
        all_types=self.graph.run('MATCH (s:Site)-[:PUBLICOU]-(n:News) WHERE n.url="'+url+'" RETURN n').data()
        news = News()
        for n in all_types:            
            news.url=n['n']['url']
        return news

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
        tipos = Tipo.select(self.graph).where(description=name)
        for tipo in tipos:
            return tipo

    def save_news(self, site, url, title, sub_title, content, autor_name, tipo):
        autor = self.save_autor(autor_name)
        t = self.get_clazz(tipo)
        news =News()
        news.site.add(site)
        news.autor.add(autor)
        news.tipo.add(t)
        news.title=title
        news.sub_title=sub_title
        news.content=content
        news.url=url
        self.graph.create(news)
        return title


    def save_autor(self, name):
        autor = Autor()
        autor.name=name        
        self.graph.push(autor)
        return autor


    def create_rel(self, node1, node2):
        self.graph.create("(s:Site)-[:PUBLICOU]->(n:News)")

    def install(self):
        self.graph.run("MATCH (n) DETACH DELETE n")
        self.graph.run("MATCH (n) DETACH DELETE n")


    def delete(self):
        self.graph.delete_all();
        tipo = Tipo()
        tipo.description='False'
        self.graph.merge(tipo)
        tipo = Tipo()
        tipo.description = 'True'
        self.graph.merge(tipo)
        tipo = Tipo()
        tipo.description = 'None'
        self.graph.merge(tipo)