from flask import Blueprint, redirect, url_for
from Caeser import Register
from models import User, db

amon_bp = Blueprint('auth', __name__)


@amon_bp.route("/", methods=["GET"])
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
        
        
        db.session.add()
        db.session.commit()
        
        return redirect(url_for('login'))