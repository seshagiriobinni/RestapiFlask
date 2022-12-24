from flask import Flask, jsonify
from flask_restful import request

app = Flask(__name__)

stores = [
    {
        "name": "My store",
        "items": [
            {
            "name": "Chair",
            "price": 15.99
        }
        ]
    }
]


@app.get('/stores')
def get_stores():
    return jsonify({'Result': stores}, 200)


@app.post('/store')
def create_store():
    request_data = request.get_json()
    print(request_data["name"])
    store = {"name": request_data["name"], "items": []}
    stores.append(store)
    return jsonify({'Result': store, 'message': 'store created successfully'}, 201)

@app.post('/store/<string:name>/item')
def create_item_in_store(name):
    request_data=request.get_json()
    for store in stores:
        print(name)
        if store['name'] == name:
            new_item={"name":request_data["name"],"price":request_data["price"]}
            store["items"].append(new_item)
            return jsonify({"new_item":new_item},201)

    return jsonify({'Message': "store not found to create item"}, 404)


@app.get('/store/<string:name>')
def get_store(name):
    for store in stores:
        print(name)
        if store['name'] == name:
            return store

    return jsonify({'Message': "store not found"}, 404)



@app.get('/store/<string:name>/item')
def get_item_in_store(name):
    for store in stores:
        print(name)
        if store['name'] == name:
            return jsonify({"items":store["items"]},200)

    return jsonify({'Message': "item not found"}, 404)


if __name__ == '__main__':
    app.run()
