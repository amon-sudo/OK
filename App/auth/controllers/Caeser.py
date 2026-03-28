from flask import Flask, render_template, redirect, url_for

from flask_wtf import FlaskForm

from wtforms import StringField, PasswordField, SubmitField

from wtforms.validators import DataRequired, Email, EqualTo
from auth.models import db, User

app =  Flask(__name__)
app.config['SECRET_KEY'] = 'amon-admiral-zheng-he'
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///app.db'

db.init_app(app)

class Register(FlaskForm):
    fname = StringField('first name', validators=[DataRequired()])
    sname = StringField('Second name', validators=[DataRequired()])
    username = StringField('username', validators=[DataRequired()])
    email = StringField('Email', validators=[DataRequired(), Email()])
    password = PasswordField('Password', validators=[DataRequired()])
    confirm = StringField('Confirm the password', validators=[DataRequired(), EqualTo('password')])
    submit = SubmitField('Register')
    
class Login(FlaskForm):
    email = StringField('Email', validators=[DataRequired()])
    password = StringField('Password', validators=[DataRequired()])
    submit = SubmitField('login')