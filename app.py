import uuid
from flask import Flask, jsonify
from flask_restful import request
from db import stores,items

app = Flask(__name__)



@app.get('/stores')
def get_stores():
    return jsonify({'Result': list(stores.values())}, 200)


@app.post('/store')
def create_store():
    store_data = request.get_json()
    store_id= uuid.uuid4().hex
    store = {**store_data,"id":store_id}
    stores[store_id]=store
    return jsonify({'Result': store, 'message': 'store created successfully'}, 201)

@app.post('/item')
def create_item_in_store():
    item_data=request.get_json()
    if item_data["store_id"] not in stores:
        return {"message":"Store not found"},404
    item_id=uuid.uuid4().hex
    item={**item_data,"id":item_id}
    items[item_id]=item

    return jsonify({'Message': "Item Created Successfully"}, 201)

@app.get('item')
def get_all_items():
    return jsonify({"items":list(items.values())})

@app.get('/store/<string:store_id>')
def get_store(store_id):
    try:
        return stores[store_id]
    except KeyError:
        return jsonify({'Message': "store_id not found"}, 404)



@app.get('/item/<string:item_id>')
def get_item(item_id):
    try:
        return items[item_id]
    except:
        return jsonify({'Message': "item not found"}, 404)


if __name__ == '__main__':
    app.run()
