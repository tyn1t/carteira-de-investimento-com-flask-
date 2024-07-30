from flask import Blueprint, render_template


home = Blueprint('home', __name__)

@home.route('/')
def Home():
    # paginn 1
    return render_template('index.html')