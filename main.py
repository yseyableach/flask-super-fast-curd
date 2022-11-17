from flask import Flask,session
from server.app2 import app2
from server.userService import userService
from server.gameService import gameService
from apidoc.swaggerApiDoc import apidocService
from flasgger import Swagger
from flask_sqlalchemy import SQLAlchemy
from flask import Flask, session
from flask_session import Session


from dotenv import dotenv_values
import sys

# import os 
# sys.path.insert(os.getcwd())
app = Flask(__name__)
# 環境變數
config = dotenv_values("models/.env")
app.config['SWAGGER'] = {
    "title": "My API",
    "description": "My API",
    "version": "1.0.2",
    "termsOfService": "",
    "hide_top_bar": True
}
app.config["SQLALCHEMY_DATABASE_URI"] = (
    "postgresql://"
    + str(config["user"])
    + ":"
    + str(config["password"])
    + "@"
    + str(config["host"])
    + ":"
    + str(config["port"])
    + "/"
    + str(config["dbname"])
)

app.config["SESSION_PERMANENT"] = False
app.config["SESSION_TYPE"] = "filesystem"
Session(app)

db = SQLAlchemy(app)
app.register_blueprint(userService, url_prefix="")
app.register_blueprint(gameService, url_prefix="")
app.register_blueprint(apidocService, url_prefix="") # 透過localhost/apidoc 產生swaggerApi文件

Swagger(app)


class user(db.Model):
    serial = db.Column(db.Integer, primary_key=True, comment="流水號1")
    name = db.Column(db.VARCHAR(64), comment="名稱")
    sex = db.Column(db.VARCHAR, comment="性別")
    LastUpdateDate = db.Column(db.DateTime, comment="資料上傳日期")

class game(db.Model):
    serial = db.Column(db.Integer, primary_key=True, comment="流水號")
    gameName = db.Column(db.VARCHAR(64), comment="遊戲名稱")
    Country = db.Column(db.VARCHAR(64), comment="國家")
    LastUpdateDate = db.Column(db.DateTime, comment="資料上傳日期")

print(game.query.filter_by(serial=5).first())


@app.route("/")
def index():
    
    return "foo"

if __name__ == "__main__":
    
    app.run(debug=True)
    session["name"] = 'sssssssssssssssssssssss'
    session["game"] = 'game'
    
    

