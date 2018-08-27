# -*- coding: utf-8 -*-
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

# 创建对象的基类:
Base = declarative_base()

# 初始化数据库连接:
engine = create_engine('mysql+pymysql://dba:111@45.78.9.17:3306/wq_01')


# 返回数据库会话
def loadSession():
    Session = sessionmaker(bind=engine)
    session = Session()
    return session
