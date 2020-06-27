from flask_sqlalchemy import SQLAlchemy
import logging as lg
from .views import app
import enum

# Create database connection object
db = SQLAlchemy(app)


class Gender(enum.Enum):
    female = 0
    male = 1
    undefined = 2


class Content(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    description = db.Column(db.String(200), nullable=False)
    gender = db.Column(db.Enum(Gender), nullable=False)

    def __init__(self, description, gender):
        self.description = description
        self.gender = gender


# db.create_all()
def init_db():
    db.drop_all()
    db.create_all()
    db.session.add(Content("Description n°1, RESULT - MALE", Gender['male']))
    db.session.add(Content("Description n°2 , RESULT - MALE", Gender['male']))
    db.session.add(Content("Description n°3 , RESULT - MALE", Gender['male']))
    db.session.add(Content("Description n°4, RESULT - MALE", Gender['male']))
    db.session.add(Content("Description n°1 , RESULT - FEMALE", Gender['female']))
    db.session.add(Content("Description n°2 , RESULT - FEMALE", Gender['female']))
    db.session.add(Content("Description n°3 , RESULT - FEMALE", Gender['female']))
    db.session.add(Content("Description n°4 , RESULT - FEMALE", Gender['female']))
    db.session.add(Content("Description n°1 , RESULT - UNDEFINED SEX", Gender['undefined']))
    db.session.commit()
    lg.warning('Database initialized!')
