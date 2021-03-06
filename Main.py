from database.NewsResources import NewsResources
from database.SiteResources import SiteResources 
import database.Neo4j as neo4j
from flask import jsonify, request
from flask import Response
from flask import Flask
import json

app = Flask("resources")
graph = neo4j.connection()
db = NewsResources(graph)
siteResources = SiteResources(graph)

@app.route("/site/<name>")
def get_site(name):
    site = siteResources.get_site(name)
    if site != None:
        content = {"name": site.name, "url": site.url}        
        return json.dumps(content)
    content = {"response": "Nenhum site foi localizado"}
    return Response(content, status=404, mimetype='application/json')

@app.route("/allSite")
def get_all_site():
    sites = siteResources.get_all_sites()  
    return jsonify(sites)
    content = {"response": "Nenhum site foi localizado"}
    return Response(content, status=404, mimetype='application/json')

@app.route("/save/site", methods=['POST'])
def save_site():
    if request.is_json:
        content = request.get_json()
        print('Site ', content['name'])
        site_name, titulo= siteResources.save_site(content['name'], content['url'])
    return jsonify(site_name, titulo)

@app.route("/site/<name>/news")
def get_news(name):
    list= db.get_all_news_from(name)    
    return json.dumps(list)

@app.route("/save/news", methods=['POST'])
def save_news():
    if request.is_json:
        content = request.get_json()
        site = siteResources.get_site(content['site'])

        if content['font'] != 'None':
            newsFont = db.get_news_by_url(content['font'])
        else:
            newsFont = None

        db.save_news(
            site,
            content['url'],
            content['title'],
            content['subTitle'],
            content['content'],
            content['autor'],
            content['datePublished'],
            content['tipo'],
            newsFont
            )
    content = {"response": "Noticia salva"}
    return Response(content, status=200, mimetype='application/json')

@app.route("/news/<url>")
def get_news_by_url(url):
    news = db.get_news_by_url(url)
    if news != None:
        content = {"title": news.title, "url": news.url}        
        return json.dumps(content)
    content = {"response": "Nenhuma noticia foi localizada"}
    return Response(content, status=404, mimetype='application/json')

@app.route("/classify/news", methods=['POST'])
def classify_news():
    if request.is_json:
        content = request.get_json()
        news = db.get_news_by_url(content['url'])
        tipo = db.get_clazz(content['tipo'])
        news.tipo.clear()
        news.tipo.add(tipo)
        db.classify_news(news)
    content = {"response": "Noticia salva"}
    return Response(content, status=200, mimetype='application/json')

@app.route("/alltype")
def get_all_type():
    list= db.get_all_types()    
    return jsonify(list)

app.run()