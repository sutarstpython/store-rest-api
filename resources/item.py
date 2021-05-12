import sqlite3
from flask_restful import Resource,reqparse
from flask_jwt import jwt_required
from models.item import ItemModel
class Item(Resource):
    parser = reqparse.RequestParser()
    parser.add_argument('price',
        type=float,
        required=True,
        help = "This is field can't blank"
    )


    @jwt_required()
    def get(self,name):
        item = ItemModel.find_item_by_name(name)
        if item:
            return item.json()
        return {'message':'item not found'},404

    def post(self,name):
        
        item = ItemModel.find_item_by_name(name)
        if item:
            return {"message":"An item with name {} already exists".format(name)}
        data=Item.parser.parse_args()
        item = ItemModel(name,data['price'])
        try:
            item.insert_item()
        except:
            return {'message','An error occured'},500
        return {'message':"Item added in db"}

    def delete(self,name):
        item = ItemModel.find_item_by_name(name)
        if item:
            item.delete_from_db()
        return {"message":"Item Deleted"}

    def put(self,name):
        data=Item.parser.parse_args()
        item = ItemModel.find_item_by_name(name)
        if Item is None:
            item = ItemModel(name,data['price'])
        else:
            item.price = data['price']
        item.save_to_db()
        return item.json()        

class itemlist(Resource):
    def get(self):
        return {'items':[item.json() for item in ItemModel.query.all]}