from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from os import path
from flask_login import LoginManager




app = Flask(__name__)
app.config['SECRET_KEY'] = 'hjshjhdjah kjshkjdhjs'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
    # app.config['SQLALCHEMY_DATABASE_URI'] = f'sqlite:///{DB_NAME}'

app.config['SQLALCHEMY_DATABASE_URI'] = f'mysql+pymysql://c22071833:Yedujayan2000@csmysql.cs.cf.ac.uk:3306/c22071833_cmt120_cw2'

DB_NAME = "database.db"
db = SQLAlchemy(app)

from .views import views
from .auth import auth


app.register_blueprint(views, url_prefix='/')
app.register_blueprint(auth, url_prefix='/')


from .models import User, Message

with app.app_context():
    db.create_all()

login_manager = LoginManager()
login_manager.login_view = 'auth.login'
login_manager.init_app(app)

@login_manager.user_loader
def load_user(id):
    return User.query.get(int(id))

