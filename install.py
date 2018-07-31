from database.NewsResources import NewsResources
from database.SiteResources import SiteResouces 
import database.Neo4j as neo4j
# import json, requests

# response = requests.get("http://localhost:5000/alltype")
# print(response.content)
graph = neo4j.connection()
db = NewsResources(graph)
db.delete()
# list = db.get_all_news_from('semprequestione')
# print(list)
