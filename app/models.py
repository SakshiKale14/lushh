
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy.dialects.postgresql import JSON, ARRAY
from sqlalchemy.orm import relationship

import datetime

db = SQLAlchemy()

class BaseModel(db.Model):
    """Base data model for all objects"""
    __abstract__ = True
  

    def __repr__(self):
        """Define a base way to print models"""
        return '%s(%s)' % (self.__class__.__name__, {
            column: value
            for column, value in self._to_dict().items()
        })

    def json(self):
        """
                Define a base way to jsonify models, dealing with datetime objects
        """
        return {
            column: value if not isinstance(value, datetime.date) else value.strftime('%Y-%m-%d')
            for column, value in self._to_dict().items()
        }

class user_details(BaseModel, db.Model):
    __tablename__ = 'user_details'
    id=db.Column(db.Integer, primary_key=True)
    user_id=db.Column(db.String(50),unique=True)
    fname=db.Column(db.String(50))
    lname=db.Column(db.String(50))
    
    email=db.Column(db.String(300),unique=True)
    password=db.Column(db.String(300),unique=True)
    cart_item=db.Column(ARRAY(JSON))
    gender=db.Column(db.String(10))
    country=db.Column(db.String(10))
    city=db.Column(db.String(10))


class prod_jwellery(BaseModel,db.Model):
    __tablename__='jewellery_table'
    id=db.Column(db.Integer,primary_key=True)
    prod_id=db.Column(db.String(12),unique=True)
    name=db.Column(db.String(50))
    price=db.Column(db.Integer)
    description=db.Column(db.String(500))
    img_url=db.Column(db.String(50))

class product_clothes(BaseModel,db.Model):
    __tablename__='cloth_table'
    id=db.Column(db.Integer,primary_key=True)
    prod_id=db.Column(db.String(12),unique=True)
    name=db.Column(db.String(50))
    price=db.Column(db.Integer)
    description=db.Column(db.String(500))
    img_url=db.Column(db.String(50))

class card_details(BaseModel,db.Model):
    __tablename__='card_details'
    id=db.Column(db.Integer,primary_key=True)
    # user table
    user_id=db.Column(db.String(50),db.ForeignKey('user_details.user_id'))
    card_no=db.Column(db.String(300),unique=True)
    card_name=db.Column(db.String(300),unique=True)
    cvv=db.Column(db.String(200),unique=True)
    expiry_date=db.Column(db.String(10))

