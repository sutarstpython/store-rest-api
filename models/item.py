import sqlite3
from db import db

class ItemModel(db.Model):
    __tablename__ = 'items'

    id= db.Column(db.Integer,primary_key=True)
    name = db.Column(db.String(80))
    price = db.Column(db.Float(precision=2))
    store_id = db.Column(db.integer,db.ForignKey('stores.id'))
    store = db.relationship('StoreModel')

    def __init__(self,name,price):
            self.name = name
            self.price = price
            
    def json(self):
        return {'name':self.name,'price':self.price}
    
    @classmethod
    def find_item_by_name(cls,name):
        return cls.query.filter_by(name=name).first()
        

    def insert_item(self):
        db.session.add(self)
        db.session.commit()