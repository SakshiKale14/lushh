from operator import ge
from flask import Blueprint, Flask , jsonify, render_template, session, request, redirect, url_for
from app.models import user_details,db
from .forms import RegistrationForm, LoginForm
import pyaes, pbkdf2, binascii, os, secrets
import random

import base64




auth_bp = Blueprint("auth_bp", __name__, template_folder="templates/auth")
row2dict = lambda r: {c.name: str(getattr(r, c.name)) for c in r.__table__.columns}
passwordSalt = b'\xed\x87\xd0!E\x82\x0c\xde\xa2\xca\xc3\xab\x18<e\x96'




@auth_bp.route("/login", methods=["GET", "POST"])
def main():
	if request.method == "POST":
		form = LoginForm()
	
		email = request.form['email']
		password = request.form['password']
		username = request.form['email']
		password = request.form['password']
		str=username[0:3]+password[0:3]
		random.seed(6)
		secret_key=''.join(random.sample(str,len(str)))
		print('@@@@@@')
		print(secret_key)
		
		
		key = pbkdf2.PBKDF2(secret_key, passwordSalt).read(32)
		print(key)
		user=user_details.query.filter_by(secret_key=key.decode('UTF-8')).first()
		if user:
			print(row2dict(user))
			iv=user['iv']
			print(iv)

		else:
			print("____NOT_____")
		
		
		
		
		


		user=user_details.query.filter_by(user_name=email).first()
		
		
		if user:
			print(row2dict(user))
			session['email'] = email
			return redirect(url_for("general_bp.home"))
		else:
			return redirect(url_for("auth_bp.signup"))
	else:
		
		return render_template("login.html", title="Login")

@auth_bp.route("/logout", methods=["GET"])
def logout():
	del session['email']
	return redirect(url_for("general_bp.home"))

@auth_bp.route("/register", methods=["GET","POST"])
def signup():
	if request.method == "POST":
	
	
		fname = request.form['fname']
		lname = request.form['lname']
		username = request.form['email']
		password = request.form['password']
		gender=request.form['gender']
		city=request.form['city']
		country=request.form['country']
		random.seed(6)

		str=username[0:3]+password[0:3]
		
		
		
		
		secret_key=''.join(random.sample(str,len(str)))
		print(secret_key)
		key = pbkdf2.PBKDF2(secret_key, passwordSalt).read(32)
		print(key)
		iv = secrets.randbits(256)
		aes = pyaes.AESModeOfOperationCTR(key, pyaes.Counter(iv))
		e_username = aes.encrypt(username)
		e_password=aes.encrypt(password)

		# create hash for username and password from this secret key==== e_username and e_password
	
		
		print('-----ENCRYPT')
		print(e_username)
		print(e_password)
		
		



		
		
	
		
	

	
		new_user= user_details(fname=fname,lname=lname,user_name=request.form['email'],password=request.form['password'],secret_key=key,gender=gender,city=city,country=country,iv=iv,e_password=e_password,e_username=e_username)
		db.session.add(new_user)
		db.session.commit()
    

		return redirect(url_for("auth_bp.main"))
	else:
		return render_template("signup.html", title ="register")

@auth_bp.route("/forgot_password", methods=["GET", "POST"])
def forgot_pass():
	return render_template("forgot_password.html", title="forgot password")