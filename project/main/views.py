from flask import Blueprint, login_required, render_template

# Config
main_blueprint = Blueprint('main', __name__,)

# Route


@main_blueprint.route('/')
@login_required
def home():
    return render_template('main/index.html')


@app.route('/welcome')  # home/welcome
def welcome():
    return render_template('main/welcome.html')  # renders welcome.html
