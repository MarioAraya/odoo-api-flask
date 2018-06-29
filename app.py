from flask import Flask
from flask_restful import Resource, Api

app = Flask(__name__)
api = Api(app)

items = []

class Item(Resource):
    def get(self, name):
        for item in items:
            if item['name'] == name:
                return item # no es necesario usar Jsonify con Flask, se pueden retornar Dictionaries
        return 

    def post(self, name):
        item = {'name': name, 'price': 12.00}
        items.append(item)
        return item

api.add_resource(Item, '/item/<string:name>') # http://127.0.0.1:5000/student/ASDF

app.run(host="0.0.0.0", port=5000)