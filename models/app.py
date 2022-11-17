from xml.etree.ElementTree import Comment
from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from dotenv import dotenv_values

"""
Migration 方式
flask db stamp head # 只更新最上一層的
flask db migrate  # 根據所連線的db進行比較
flask db upgrade  # 更新結果到DB
"""



# 環境變數
config = dotenv_values(".env")

app = Flask(__name__)

# app.config[
#     "SQLALCHEMY_DATABASE_URI"
# ] = "postgresql://ad1500@postgre-wicruiting-dev:VD1500wistron@postgre-wicruiting-dev.postgres.database.azure.com:5432/DB-wicruiting-dev"
print(config)
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


db = SQLAlchemy(app)
migrate = Migrate(app, db)
print(db.attribute)

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


# '''
# attribute 設定的文件
# https://flask-sqlalchemy.palletsprojects.com/en/2.x/models/
# '''
