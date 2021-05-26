from flask import Blueprint, Flask , jsonify, render_template, session, request, redirect, url_for
from app.models import user_details,db
from .forms import RegistrationForm, LoginForm
import pyaes, pbkdf2, binascii, os, secrets
from app.aes import key,iv


auth_bp = Blueprint("auth_bp", __name__, template_folder="templates/auth")
row2dict = lambda r: {c.name: str(getattr(r, c.name)) for c in r.__table__.columns}



@auth_bp.route("/login", methods=["GET", "POST"])
def main():
	if request.method == "POST":
		form = LoginForm()
	
		email = request.form['email']
		password = request.form['password']
		


		user=user_details.query.filter_by(email=email).first()
		
		
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
		email = request.form['email']
		password = request.form['password']
		aes = pyaes.AESModeOfOperationCTR(key, pyaes.Counter(iv))
		ciphertext1 = aes.encrypt(email)
		ciphertext2 = aes.encrypt(email)
		print('______')
		print(ciphertext1)
		print(ciphertext2)
		
	

	
		new_user= user_details(fname=fname,lname=lname,email=ciphertext1,password=ciphertext2,)
		db.session.add(new_user)
		db.session.commit()
    

		return redirect(url_for("auth_bp.main"))
	else:
		return render_template("signup.html", title ="register")

@auth_bp.route("/forgot_password", methods=["GET", "POST"])
def forgot_pass():
	return render_template("forgot_password.html", title="forgot password")