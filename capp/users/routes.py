from flask import render_template, Blueprint

users=Blueprint('users',__name__)

@users.route('/login')
def login():
  return render_template('users/login.html', title="login")

@users.route('/register')
def register():
  return render_template('users/register.html', title="register")