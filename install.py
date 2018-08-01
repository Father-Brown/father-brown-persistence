from database.NewsResources import NewsResources
from database.SiteResources import SiteResources 
from database.Config import Config
import database.Neo4j as neo4j


graph = neo4j.connection()
db = NewsResources(graph)
siteResources = SiteResources(graph)
config = Config(graph)
config.install()

# site = siteResources.get_site('Desconhecido')
# db.save_news(
#             site,
#             'aaa',
#             'Titulo',
#             'eita',
#             'Eita vei',
#             'Abrilina',
#             '',
#             'None',
#             None
#             )
# news = db.get_news_by_url('aaa')
# db.save_news(
#             site,
#             'abbb',
#             'Titulo2',
#             'eitabbb',
#             'Eita veibbbb',
#             'Abrilina',
#             '',
#             'None',
#             news
#             )