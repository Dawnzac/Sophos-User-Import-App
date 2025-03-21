from flask import Blueprint, render_template, request, redirect, url_for, flash
from flask_login import login_user, logout_user, login_required, current_user
from .forms import LoginForm, UserImportForm
from .models import User

app_routes = Blueprint('app_routes', __name__)

@app_routes.route('/login', methods=['GET', 'POST'])
def login():
    form = LoginForm()
    if form.validate_on_submit():
        user = User.query.filter_by(username=form.username.data).first()
        if user and user.check_password(form.password.data):
            login_user(user)
            flash('Login successful!', 'success')
            return redirect(url_for('app_routes.dashboard'))
        flash('Invalid username or password', 'danger')
    return render_template('login.html', form=form)

@app_routes.route('/logout')
@login_required
def logout():
    logout_user()
    flash('You have been logged out.', 'info')
    return redirect(url_for('app_routes.login'))

@app_routes.route('/dashboard')
@login_required
def dashboard():
    return render_template('dashboard.html', user=current_user)

@app_routes.route('/user-import', methods=['GET', 'POST'])
@login_required
def user_import():
    form = UserImportForm()
    if form.validate_on_submit():
        # Logic for importing users goes here
        flash('Users imported successfully!', 'success')
        return redirect(url_for('app_routes.dashboard'))
    return render_template('user_import.html', form=form)