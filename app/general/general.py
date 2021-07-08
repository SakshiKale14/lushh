from flask import Flask, Blueprint, render_template, request, jsonify, url_for, redirect
from flask.globals import session
from app.models import user_details,db

import requests
import json
general_bp = Blueprint("general_bp", __name__ , template_folder="templates/general", static_url_path="/static")
no='0'
@general_bp.before_request
def before_request():
    
    if 'email' in session:
        user=user_details.query.filter_by(user_name=session['email']).first()
        if user.cart_item:
            no=str(len(user.cart_item))
        else:
            no=0
@general_bp.route("/")
def home():
   
    
    print(no)
    return render_template("index.html", title="Home",cartNo=no)




@general_bp.route("/search")
def search():
    query = request.args['keyword']
    products = requests.get("http://localhost:5000/api/products/groceries/"+query)
    return render_template("search_results.html",search_results={"products":products.json(), "number":len(products.json())}, title=query)

