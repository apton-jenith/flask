from flask import Flask 
from flask_sqlalchemy import SQLAlchemy
from flask_user import UserManager, UserMixin, SQLAlchemyAdapter

app = Flask(__name__)

app.config['SECRET_KEY'] = 'randomstring'
app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql+pymysql://root:Current-Root-Password@localhost/our_users'
app.config['CSRF_ENABLED'] = True 
app.config['USER_ENABLE_EMAIL'] = False

db = SQLAlchemy(app)

class User(db.Model, UserMixin):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(50), nullable=False, unique=True)
    password = db.Column(db.String(255), nullable=False, server_default='')
    active = db.Column(db.Boolean(), nullable=False, server_default='0')

db_adapter = SQLAlchemyAdapter(db, User)
user_manager = UserManager(db_adapter, app)

if __name__ ==  '__main__':
    app.run(debug=True)