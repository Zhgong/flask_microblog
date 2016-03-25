from flask import Flask
from flask_sqlalchemy import SQLAlchemy

# ------------------------------------------- #
# tutorial                                    #
# from flask.ext.sqlalchemy import SQLAlchemy #
# ------------------------------------------- #


app = Flask(__name__)
app.config.from_object('config')
db = SQLAlchemy(app)

from blog import views, models
