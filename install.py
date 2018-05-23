from database.DataBase import DataBase
import json, requests

response = requests.get("http://localhost:5000/alltype")
print(response.content)
# db = DataBase()
# db.delete()
