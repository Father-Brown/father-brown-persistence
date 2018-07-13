import py2neo
from py2neo import Graph
from database.model.Model import Site
from database.model.Model import News
from database.model.Model import Tipo

class SiteResouces:

    def __init__(self, graph):        
        self.graph = graph

    def get_all_sites(self):        
        all_types=self.graph.run('MATCH (s:Site) RETURN s').data()
        dataSet=list()
        for n in all_types:
            dataSet.append({'name':n['s']['name'], 'url':n['s']['url']})

        return dataSet

    def get_site(self, name):
        sites = Site.select(self.graph).where(name=name)
        print(sites)
        for site in sites:
            return site

    def save_site(self, site_name, url):
        site=Site()
        site.name=site_name
        site.url=url
        self.graph.push(site)
        return site_name, url