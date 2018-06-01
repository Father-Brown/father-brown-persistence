from database.DataBase import DataBase
from flask import jsonify, request
from flask import Response
from flask import Flask
import json

app = Flask("resources")

db = DataBase()

@app.route("/site/<name>")
def get_site(name):
    site = db.get_site(name)
    if site != None:
        content = {"name": site.name, "url": site.url}        
        return json.dumps(content)

    content = {"response": "Nenhum site foi localizado"}
    return Response(content, status=404, mimetype='application/json')

@app.route("/save/site", methods=['POST'])
def save_site():
    if request.is_json:
        content = request.get_json()
        print('Site ', content['name'])
        site_name, titulo= db.save_site(content['name'], content['url'])
    return jsonify(site_name, titulo)

@app.route("/save/news", methods=['POST'])
def save_news():
    if request.is_json:
        content = request.get_json()
        site_name, url= db.save_news(content['site'], content['url'], content['title'], content['subTitle'],
                                     content['content'], content['tipo'])
    return jsonify(site_name, url)

@app.route("/site/<name>/news")
def get_news(name):
    list= db.get_all_news_from(name)    
    return json.dumps(list)

@app.route("/alltype")
def get_all_type():
    list= db.get_all_types()    
    return jsonify(list)

app.run()