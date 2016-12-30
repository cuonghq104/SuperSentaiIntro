from flask import Flask
import mlab

from mongoengine import *
from flask_restful import reqparse, Resource, Api

import json

mlab.connect()


class Sentai(Document):
    name = StringField()
    numberOfMembers = StringField()
    theme = StringField()


# s = Sentai(name = "Kaizoku sentai Gokaiger", numberOfMembers = "6", theme = "Pirates")
# s.save()

# for s in Sentai.objects:
#     print(s.to_json())

app = Flask(__name__)
api = Api(app)
parser = reqparse.RequestParser()
parser.add_argument("name", type = str, location = "json")
parser.add_argument("numberOfMembers", type = str, location = "json")
parser.add_argument("theme", type = str, location = "json")

@app.route('/')
def hello_world():
    return 'Hello World!'

class SentaiListRes(Resource):
    def get(self):
        return mlab.list2json(Sentai.objects)
    def post(self):
        args = parser.parse_args()
        name = args["name"]
        numberOfMembers = args["numberOfMembers"]
        theme = args["theme"]
        new_sentai = Sentai(name = name, numberOfMembers = numberOfMembers, theme = theme)
        new_sentai.save()
        return mlab.item2json(new_sentai)

class SentaiRes(Resource):

    def get(self, sentai_id):
        all_sentai = Sentai.objects
        found_sentai = all_sentai.with_id(sentai_id)
        return mlab.item2json(found_sentai)

    def delete(self, sentai_id):
        all_sentai = Sentai.objects
        found_sentai = all_sentai.with_id(sentai_id)
        found_sentai.delete()
        return {"Status": "Deleted", "Code": "1"}, 200

    def put(self, sentai_id):
        args = parser.parse_args()
        name = args["name"]
        numberOfMembers = args["numberOfMembers"]
        theme = args["theme"]
        all_sentai = Sentai.objects
        found_sentai = all_sentai.with_id(sentai_id)
        found_sentai.update(set__name = name, set__numberOfMembers = numberOfMembers, set__theme = theme)
        return mlab.item2json(found_sentai)

api.add_resource(SentaiListRes, "/api/sentai")
api.add_resource(SentaiRes, "/api/sentai/<sentai_id>")

if __name__ == '__main__':
    app.run()
