from flask import jsonify, request
from database.DataBase import DataBase
from flask import Flask
import json

app = Flask("resources")

db = DataBase()

@app.route("/site/<name>")
def get_site(name):    
    list= db.get_site(name)
    for  s in list:
        print(s)
    return json.dumps(list)

@app.route("/save/site", methods=['POST'])
def save_site():
    if request.is_json:
        content = request.get_json()
        print('Site ', content['name'])
        site_name, url= db.save_site(content['name'], content['url'])
    return jsonify(site_name, url)


@app.route("/")
def get_news():
    list= db.get_all_news_from("teste")
    print(type(list))
    return jsonify(list)



@app.route("/save/news", methods=['POST'])
def save_news():
    if request.is_json:
        content = request.get_json()
        print(content['site'])

        site_name, url= db.save_news(content['site'], content['url'], content['title'], content['subTitle'],
                                     content['content'], content['tipo'])
    return jsonify(site_name, url)




@app.route("/alltype")
def get_all_type():
    list= db.get_all_types()    
    return jsonify(list)

app.run()