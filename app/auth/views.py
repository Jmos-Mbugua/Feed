from flask import render_template,url_for,flash,redirect,request
from . import auth
from flask_login  import login_user,login_required,logout_user
from .form import LoginForm,RegisterForm
from ..models import User
from flask_login import login_user
from .. import db


@auth.route('/login',methods=["GET","POST"])
def login():
    form = LoginForm()
    user = User.query.filter_by(username = form.username.data).first()
    if user != None and user.verify_password(form.password.data):
        login_user(user,form.remember)
        return redirect(request.args.get('next') or url_for('main.index'))
        flash('Invalid username and password')
    return render_template('auth/login.html',loginform= form)

