import sqlite3
from db import db

class StoreModel(db.Model):
    __tablename__ = 'stores'

    id= db.Column(db.Integer,primary_key=True)
    name = db.Column(db.String(80))
    items = db.realtionship('ItemModel')

    def __init__(self,name):
            self.name = name
            
    def json(self):
        return {'name':self.name,'items':self.items}
    
    @classmethod
    def find_item_by_name(cls,name):
        return cls.query.filter_by(name=name).first()
        

    def insert_item(self):
        db.session.add(self)
        db.session.commit()