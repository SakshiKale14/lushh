from flask import Flask, abort , session, redirect
from app.general.general import general_bp
from app.ajax.ajax import ajax_bp
from app.products.products import  products_bp
from app.auth.auth import auth_bp	
from app.cart.cart import cart_bp
from flask_cors import CORS
from app.models import db
from app.aes import key

app = Flask(__name__)
cors = CORS(app)
app.secret_key = "hhdhdhdhdh7788768"
print('======')
print(key)


app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://postgres:password@localhost/bazar'
db.init_app(app)




@app.before_request
def run():
	if 'email' in session:
		redirect("/")
	else:
		redirect("/auth/login")
app.register_blueprint(general_bp)  
app.register_blueprint(ajax_bp, url_prefix="/ajax")
app.register_blueprint(products_bp, url_prefix="/products")
app.register_blueprint(auth_bp, url_prefix="/auth")
app.register_blueprint(cart_bp, url_prefix="/cart")

# cart page (cart click)
#checkout page (buy now)
#replace logo
#log out
#see db
#credit card detail page

