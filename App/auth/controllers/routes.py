from flask import Blueprint, redirect, url_for, render_template
from .Caeser import Register, Login
from auth.models import User, db

amon_bp = Blueprint( __name__)


@amon_bp.route("/", methods=["POST","GET"])
def regi():
    form = Register()
    if form.validate_on_submit():
        fname = form.fname.data
        sname = form.sname.data
        username = form.username.data
        email = form.email.data
        password = form.password.data
        
        
        newser = User(
            fname  = fname, sname = sname, username = username, 
            email = email)
        newser.set_damn_password(password)
        
        
        db.session.add(newser)
        db.session.commit()
        
    return redirect(url_for('login'))
    
    
@amon_bp.route("/Login", methods=["POST", "GET"])
def login():
    form = Login()
 
    
    if form.validate_on_submit():
           email = form.email.data
           password = form.password.data
           
           
           user = User.query.filter_by(email=email).first()
           if user and user.check_damn_passeord(password):
               return "welcom buana. Login succesfully"
           else:
               return "inavalid username or password"
           
    return render_template(url_for("login.html", form=form))