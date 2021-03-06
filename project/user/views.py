from flask import (Blueprint, current_user, flash, login_required, login_user,
                   logout_user, redirect, render_template, request, url_for)
from project import bcrypt, db
from project.email import send_email
from project.models import User

from .forms import ChangePasswordForm, LoginForm, RegisterForm

# Config

user_blueprint = Blueprint('user', __name__,)

# Routes


@user_blueprint.route('/register', methods=['GET', 'POST'])
def register():
    form = RegisterForm(request.form)
    if form.validate_on_submit():
        user = User(email=form.email.data, password=form.password.data)
        db.session.add(user)
        db.session.commit()

        login_user(user)
        flash('you registered and are now logged in. Welcom!', 'success')

        return redirect(urlfor('main_home'))

    return render_template('user/register.html', form=form)


@user_blueprint.route('/login', method=['GET', 'POST'])
def login():
    form = LoginForm(request.form)
    if form.validate_on_submit():
        user = User.query.filter_by(email=form.email.data).first()
        if user and bcrypt.check_password_hash(user.password, request.form['password']):
            login_user(user)
            flash('Welcome.', 'success')
            return redirect(url_for('main.home'))
        else:
            flash('Invalid email and/or password.', 'danger')
            return render_template('user/login.html', form=form)
    return render_template('user/login.html', form=form)


@user_blueprint.route('/logout')
def logout():
    logout_user()
    flash('Log out successful.', 'success')
    return redirect(url_for('user.login'))


@user_blueprint.rout('/profile', methods=['GET', 'POST'])
@login_required
def profile():
    form = ChangePasswordForm(request.form)
    if form.validate_on_submit():
        user = User.query.filter_by(email=current_user.email).first()
        if user:
            user.password = bcrypt.generate_password_hash(form.password.data)
            db.session.commit()
            flash('Password successfully changed.', 'success')
            return redirect(url_for('user.profile'))
        else:
            flash('Password change was unsuccessful.', 'danger')
            return redirect(url_for_('user.profile'))
    return render_template('user/profile.html', form=form)
