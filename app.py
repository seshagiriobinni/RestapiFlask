import uuid
from flask import Flask, jsonify
from flask_smorest import abort
from flask_restful import request
from db import stores,items

app = Flask(__name__)



@app.get('/stores')
def get_stores():
    return jsonify({'Result': list(stores.values())}, 200)


@app.post('/store')
def create_store():
    store_data = request.get_json()
    if "name" not in store_data:
        abort(400,message="Bad request. Ensure 'name' is included in the JSON payload")
    for store in stores:
        if store_data["name"]==store["name"]:
            abort(400,message="Store already existed")
    store_id= uuid.uuid4().hex
    store = {**store_data,"id":store_id}
    stores[store_id]=store
    return jsonify({'Result': store, 'message': 'store created successfully'}, 201)

@app.post('/item')
def create_item_in_items():
    item_data=request.get_json()
    if (
        "price" not in item_data
        or "store_id" not in item_data
        or "name" not in item_data
    ):
        abort(400,"Bad request. Ensure 'price','store_id','name' are included in the JSON payload")
    for item in items.values():
        if (item_data["name"]==item["name"] and item_data["store_id"]==item["store_id"]):
            abort(400,message="item already existed")
    if item_data["store_id"] not in stores:
        abort(404,message="Store not found.")
    item_id=uuid.uuid4().hex
    item={**item_data,"id":item_id}
    items[item_id]=item

    return jsonify({'Message': "Item Created Successfully"}, 201)

@app.put('/item/<string:item_id>')
def update_item_in_items(item_id):
    item_data=request.get_json()
    if (
        "price" not in item_data
        
        or "name" not in item_data
    ):
        abort(400,"Bad request. Ensure 'price','name' are included in the JSON payload")
    try:
        item=items[item_id]
        item|=item_data
        return item
    except:
        abort(404,message="Item not found")

@app.get('/item')
def get_all_items():
    return jsonify({"items":list(items.values())})


@app.get('/store/<string:store_id>')
def get_store(store_id):
    try:
        return stores[store_id]
    except KeyError:
        abort(404,message="Store not found.")

@app.delete('/store/<string:store_id>')
def delete_store(store_id):
    try:
        del stores[store_id]
        return {"message":"store deleted successfully"}
    except KeyError:
        abort(404,message="Store not found.")

@app.delete('/item/<string:item_id>')
def delete_item(item_id):
    try:
        del items[item_id]
        return {"message":"item deleted successfully"}
    except:
        abort(404,message="Item not found.")

@app.get('/item/<string:item_id>')
def get_item(item_id):
    try:
        return items[item_id]
    except:
        abort(404,message="Item not found.")


if __name__ == '__main__':
    app.run()
