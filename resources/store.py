import uuid
from flask import request
from flask.views import MethodView
from flask_smorest import Blueprint,abort
from db import stores

blp= Blueprint("Stores",__name__,description="Operations on stores")

@blp.route('/store/<string:store_id>')
class Stores(MethodView):
    def get(self,store_id):
        try:
            return stores[store_id]
        except KeyError:
            abort(404,message="Store not found.")

    def delete(self,store_id):
        try:
            del stores[store_id]
            return {"message": "store deleted successfully"}

        except KeyError:
            abort(404,message="Store not found.")

