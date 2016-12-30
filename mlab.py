#mongodb://<dbuser>:<dbpassword>@ds027425.mlab.com:27425/techfood
import mongoengine

#mongodb://<dbuser>:<dbpassword>@ds149258.mlab.com:49258/sentai

host = "ds149258.mlab.com"
port = 49258
db_name = "sentai"
user_name = "cuong"
password = "cuong"

def connect():
    mongoengine.connect(db_name, host=host, port=port, username=user_name, password=password)

def list2json(l):
   import json
   return [json.loads(item.to_json()) for item in l]

def item2json(item):
   import json
   return json.loads(item.to_json())