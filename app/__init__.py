from flask import Flask, render_template
from flask.ext.sqlalchemy import SQLAlchemy
import flask.ext.restless

app = Flask(__name__)
app.config.from_object('config')
db = SQLAlchemy(app)
from app.auth_module.controllers import auth_module
from app.database_module.controllers import database_module

app.register_blueprint(auth_module)
app.register_blueprint(database_module)

#create db tables if required
#db.create_all()

manager = flask.ext.restless.APIManager(app, flask_sqlalchemy_db=db)
manager.create_api(Event, method=['GET'])
manager.create_api(ExperimentData, method=['GET'])
manager.create_api(Sensor, method=['GET'])
manager.create_api(Packages, method=['GET'])

