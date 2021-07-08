from flask import Blueprint, render_template
from flask.globals import request
from requests.sessions import session
from operator import ge
from flask import Blueprint, Flask , jsonify, render_template, session, request, redirect, url_for
from app.models import user_details,db


row2dict = lambda r: {c.name: str(getattr(r, c.name)) for c in r.__table__.columns}
cart_bp = Blueprint("cart_bp", __name__, template_folder = "templates")
@cart_bp.before_request
def before_request():
	
	
	if 'email' in session:
		user=user_details.query.filter_by(user_name=session['email']).first()
		global no
		if user.cart_item:
			
			no=str(len(user.cart_item))
			print('-------')
			print(no)
		else:
			
			no='0'

@cart_bp.route("/view")
def main():
	if session['email']:
			print('cartttttttttt')
			user=user_details.query.filter_by(user_name=session['email']).first()
			print(user.cart_item)
			return render_template("cart/view.html",title='Cart',items=user.cart_item,cartNo=no)
	else:
			# get cart items for user from db
			return redirect(url_for("general_bp.home"))
	

@cart_bp.route('/add_to_cart',methods=['POST'])
def addtocart():
	if request.method=='POST':
		if session['email']:
			print('---cart----')
			items=[]
			
			print(request.get_json())
			# add to cart in db
			user_email=session['email']
			user=user_details.query.filter_by(user_name=user_email).first()
			print("==============")
			print(user.cart_item)
			if user.cart_item==None:
				
				items.append(request.get_json())
				print('items')
				print(items)
				
			
			else:
				print('append')
				items=user.cart_item
				print('old arr')
				items.append(request.get_json())
				print(items)
				
			user_details.query.filter_by(user_name=user_email).update(dict(cart_item=items))
			db.session.commit()
				
			
			

			return '4'
		else:
			return redirect(url_for("general_bp.home"))
	
		


	

