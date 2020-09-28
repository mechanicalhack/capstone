import os
from sqlalchemy import Column, String, create_engine, DateTime, Integer
from flask_sqlalchemy import SQLAlchemy
import json

database_name = "casting_agency"
database_path = "postgres://{}/{}".format('localhost:5432', database_name)

db = SQLAlchemy()

def setup_db(app, database_path=database_path):
    app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql-parallel-65214'
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
    db.app = app
    db.init_app(app)
    # db.create_engine()


'''
Movies with attributes title and release date
'''
class Movies(db.Model):
    id = Column(Integer, primary_key=True)
    title = Column(String)
    releaseDate = Column(DateTime)

    def __init__(self, title, releaseDate):
        self.title = title
        self.releaseDate = releaseDate

    def format(self):
        return {
            'id': self.id,
            'title': self.title,
            'releaseDate': self.releaseDate
        }
    
    def insert(self):
        db.session.add(self)
        db.session.commit()
    
    def delete(self):
        db.session.delete(self)
        db.session.commit()
    
    def update(self):
        db.session.commit()

'''
Actors with attributes name, age and gender
'''
class Actors(db.Model):
    id = Column(Integer, primary_key=True)
    name = Column(String)
    age = Column(Integer)
    gender = Column(String)

    def __init(self, name, age, gender):
        self.name = name
        self.age = age
        self.gender = gender
    
    def format(self):
        return {
            'id': self.id,
            'name': self.name,
            'age': self.age,
            'gender': self.gender
        }

    def insert(self):
        db.session.add(self)
        db.session.commit()
    
    def delete(self):
        db.session.delete(self)
        db.session.commit()
    
    def update(self):
        db.session.commit()

# TODO How do I want to respresent it???
    # def __repr__(self):
    #     return 