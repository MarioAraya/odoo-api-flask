from flask import Flask, request
from flask_restful import Resource, Api

app = Flask(__name__)
app.secret_key = 'mario'
api = Api(app)

items = []

class Item(Resource):
    def get(self, name):
        item = next(filter(lambda => x: x.get('name')==name, items), None)
        return { 'item': item }, 200 if item else 404

    def post(self, name):
        item = next(filter(lambda => x: x.get('name')==name, items), None)
        if item:
            return { 'message', "An item with name {} already exists.".format(name)}, 400

        data = request.get_json()
        item = {'name': name, 'price': data['price']}
        items.append(item)
        return item, 201

class ItemsList(Resource):
    def get(self):
        return {'items': items}

api.add_resource(Item, '/item/<string:name>') # http://127.0.0.1:5000/item/ASDF
api.add_resource(ItemsList, '/items')         # http://127.0.0.1:5000/items

app.run(host="0.0.0.0", port=5000)