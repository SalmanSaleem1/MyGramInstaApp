from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_bcrypt import Bcrypt
from flask_login import LoginManager


app = Flask(__name__,template_folder='template')
app.secret_key = '123456789'
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///insta.db'
db = SQLAlchemy(app)
bcrypt = Bcrypt(app)
login_manager = LoginManager(app)
login_manager.login_view = 'login'
login_manager.login_message_category = 'info'


from insta.user.routes import user


app.register_blueprint(user)
