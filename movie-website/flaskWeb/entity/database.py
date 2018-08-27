from flask import Flask
from flask_sqlalchemy import SQLAlchemy

import os

basedir = os.path.abspath(os.path.dirname(__file__))

# 默认情况下，InnoDB 引擎单一字段索引的长度最大为 767 字节
# 无法指定默认时间： 因为mysql的datetime类型的数据不支持函数, 所以没法指定默认值位当前时间

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql+pymysql://dba:111@45.78.9.17:3306/wq_01?charset=utf8'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = True

db = SQLAlchemy(app)

# # 暂时，等待输入db.create_all() 创建数据库等
# try:
#     code.interact(local=locals())
# except SystemExit:
#     print('exit......')
