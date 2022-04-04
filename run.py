from flask import Flask, render_template
from datetime import timedelta
from flask_restx import Api, Resource
from users.user_account import user_account
from users.user_info import user_info
from users.mainpage import mainpage
from users.cal import calorie
from users.image import image
from flask_cors import CORS
from flask_sqlalchemy import SQLAlchemy
from controll.user_account_model import user_account_db
from controll.user_info_model import user_info_db
from controll.image_model import image_db


app = Flask(__name__)
app.secret_key = 'any random string'
app.config["SQLALCHEMY_DATABASE_URI"] = "mysql+pymysql://lab03:lab03@localhost:3306/user"
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False
app.config['PERMANENT_SESSION_LIFETIME'] = timedelta(days=7)
api = Api(app)
CORS(app)
user_account_db.init_app(app)
user_account_db.app = app
user_account_db.create_all()
user_info_db.init_app(app)
user_info_db.app = app
image_db.init_app(app)
image_db.app = app
image_db.create_all()
user_info_db.create_all()
api.add_namespace(user_account, '/user_account')
api.add_namespace(user_info, '/user_info')
api.add_namespace(mainpage, '/mainpage')
api.add_namespace(calorie, '/calorie')
api.add_namespace(image, '/image')


if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port='2888')
