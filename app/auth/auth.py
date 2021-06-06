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
		
	
		
		username = request.form['email']
		password = request.form['password']
		str=username[0:3]+password[0:3]
		random.seed(6)
		secret_key=''.join(random.sample(str,len(str)))
		
		
		
		key = pbkdf2.PBKDF2(secret_key, passwordSalt).read(32)
	

		secretStr=binascii.hexlify(key).decode('utf-8')
		
		user=user_details.query.filter_by(secret_key=secretStr).first()
		if user:
			user=row2dict(user)
			iv=int(user['iv'])
			aes = pyaes.AESModeOfOperationCTR(key, pyaes.Counter(iv))
			tryUser=aes.encrypt(username)
			tryPw=aes.encrypt(password)
			
			
			encUser=user_details.query.filter_by(e_username=binascii.hexlify(tryUser).decode('utf-8'),e_password=binascii.hexlify(tryPw).decode('utf-8')).first()
			if encUser:

				session['email'] = row2dict(encUser)['user_name']
				print('milgaya')
				return redirect(url_for("general_bp.home"))
			else:
				return redirect(url_for("auth_bp.signup"))


			

		else:
			print("____NOT_____")
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
		print(binascii.hexlify(key).decode('utf-8'))
		print(type(binascii.hexlify(key).decode('utf-8')))		
		iv = secrets.randbits(256)
		aes = pyaes.AESModeOfOperationCTR(key, pyaes.Counter(iv))
		e_username = aes.encrypt(username)
		e_password=aes.encrypt(password)

		# create hash for username and password from this secret key==== e_username and e_password
	
		
		print('-----ENCRYPT')
		print(e_username)
		print(e_password)
		
		



		
		
	
		
	

	
		new_user= user_details(fname=fname,lname=lname,user_name=request.form['email'],password=request.form['password'],secret_key=binascii.hexlify(key).decode('utf-8'),gender=gender,city=city,country=country,iv=iv,e_password=binascii.hexlify(e_password).decode('utf-8'),e_username=binascii.hexlify(e_username).decode('utf-8'))
		db.session.add(new_user)
		db.session.commit()
    

		return redirect(url_for("auth_bp.main"))
	else:
		return render_template("signup.html", title ="register")

@auth_bp.route("/forgot_password", methods=["GET", "POST"])
def forgot_pass():
	return render_template("forgot_password.html", title="forgot password")