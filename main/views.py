from flask import render_template, Blueprint
from flask.ext.login import login_required


# Config
main_blueprint = Blueprint('main', __name__,)

# Route


@main_blueprint.route('/')
@login_required
def home():
    return rendere_template('main/index.html')


@app.route('/welcome')  # home/welcome
def welcome():
    return render_template('welcome.html')  # renders welcome.html
