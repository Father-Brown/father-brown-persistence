import py2neo
from py2neo import Graph
from database.model.Model import Site
from database.model.Model import News
from database.model.Model import Autor
from database.model.Model import Tipo
from database.NewsResources import NewsResources
from database.SiteResources import SiteResources 

class Config:
    ORIGINAL = 'Original'
    FAKE = 'Fake'
    NONE = 'None'
    def __init__(self, graph):       
        self.graph = graph
        self.newsResources = NewsResources(graph)
        self.siteResources = SiteResources(graph)

    def install(self):
        self.delete()
        self.siteResources.save_site('Desconhecido', '')
        tipo = Tipo()
        tipo.description = self.FAKE
        self.graph.merge(tipo)
        tipo = Tipo()
        tipo.description = self.ORIGINAL
        self.graph.merge(tipo)
        tipo = Tipo()
        tipo.description = self.NONE
        self.graph.merge(tipo)
        self.newsResources.save_autor('Desconhecido')

    def delete(self):
        self.graph.run("MATCH (n) DETACH DELETE n")
        