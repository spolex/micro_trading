from flask import Blueprint, render_template

home_bp = Blueprint('home', __name__, static_url_path="home")


@home_bp.route('/')
def index():
    return render_template('home/index.html')
