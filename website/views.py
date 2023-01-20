from flask import Blueprint,render_template
from flask_login import login_required, current_user


views= Blueprint('views', __name__)

@views.route('/')
def home():
    return render_template("home.html",user=current_user)

@views.route('/report')
def report():
    return render_template("report.html",user=current_user)


