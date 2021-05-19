from flask import Blueprint, render_template, request, flash
from .models import User
from werkzeug.security import generate_password_hash, check_password_hash


auth = Blueprint('auth', __name__)

@auth.route('/login', methods=['GET', 'POST'])
def auth_page():
    data = request.form
    print(data)
    return render_template('login.html')

@auth.route('/logout')
def logout():
    return '<p>logout</p>'

@auth.route('/register', methods=['GET', 'POST'])
def register():
    if request.method == 'POST':
        user_name = request.form.get('username')
        email = request.form.get('email')
        password1 = request.form.get('password1')
        password2 = request.form.get('password2')

        if len(user_name) < 2:
            flash('User Name must be greater than 1 character', category='error')
        elif len(email) < 4:
            flash('Email Address must be greater than 3 characters', category='error')
        elif password1 != password2:
            flash('Password don\'t match', category='error')
        elif len(password1) < 7:
            flash('Password must be greater than 6 characters', category='error')
        else:
            new_user = User(email=email, user_name=user_name, password=password1)
            flash('Account Create',category='success')
    return render_template('register.html')
