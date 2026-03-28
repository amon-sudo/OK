from flask import Blueprint, redirect, url_for, render_template
from .Caeser import Register, Login
from auth.models import User, db

amon_bp = Blueprint("auth", __name__, url_prefix="/auth")


@amon_bp.route("/register", methods=["POST","GET"])
def regi():
    form = Register()
    if form.validate_on_submit():
        fname = form.fname.data
        sname = form.sname.data
        username = form.username.data
        email = form.email.data
        password = form.password.data
        
        print(form.errors) 
        newser = User(
            fname  = fname, sname = sname, username = username, 
            email = email)
        newser.set_damn_password(password)
        
        
        db.session.add(newser)
        db.session.commit()
        
        return redirect(url_for('auth.login'))
    else:
        print(form.errors)
    return render_template("register.html", form=form)
    
    
@amon_bp.route("/login", methods=["POST", "GET"])
def login():
    form = Login()
 
    
    if form.validate_on_submit():
           email = form.email.data
           password = form.password.data
           
           
           user = User.query.filter_by(email=email).first()
           if user and user.check_damn_password(password):
               return "welcom buana. Login succesfully"
           else:
               return "inavalid username or password"
           
    return render_template("Login.html", form=form)