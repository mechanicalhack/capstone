import os
from sqlalchemy import Column, String, create_engine, DateTime, Integer
from flask_sqlalchemy import SQLAlchemy
import json

database_filename = "database.db"
project_dir = os.path.dirname(os.path.abspath(__file__))
database_path = "sqlite:///{}".format(os.path.join(project_dir, database_filename))

db = SQLAlchemy()

def setup_db(app, database_path=database_path):
    app.config['SQLALCHEMY_DATABASE_URI'] = database_path
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
    releaseDate = DateTime

    def __init__(self, title, releaseDate):
        self.title = title
        self.releaseDate = releaseDate

    def format(self):
        return {
            'id': self.id,
            'title': self.title,
            'releaseDate': self.releaseDate
        }

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
        db.sesstion.commit()
    
    def delete(self):
        db.session.delete(self)
        db.session.commit()
    
    def update(self):
        db.session.commit()

# TODO How do I want to respresent it???
    # def __repr__(self):
    #     return 