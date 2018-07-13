import py2neo
from py2neo import Graph

def connection():
    host = "172.17.0.2"
    py2neo.authenticate(host+":7474", "neo4j", "st1215")
    return Graph("http://"+host+":7474/db/data/")