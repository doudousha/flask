# from datetime import datetime
#
# from sqlalchemy import Column, Integer, String, Text, DateTime
# from . import Base, loadSession
# from sqlalchemy.orm import sessionmaker
#
#
# class Movie(Base):
#     __tablename__ = 'movie'
#     id = Column('id', Integer, primary_key=True)
#     title = Column('title', String)
#     content = Column(Text)
#     createTime = Column(DateTime, nullable=False, default=datetime.utcnow)
#     updateTime = Column(DateTime, nullable=False, default=datetime.utcnow)
#
#
# # String 需要指定长度参数，否则报错
#
#
# class MoviescrapyPipeline(object):
#     def process_item(self, item, spider):
#         movie = Movie()
#         movie.title = item['title']
#         movie.content = item['content']
#
#         print('数据--%s' % (movie.title))
#         print('内容--%s' % (movie.content))
#
#         session = loadSession()
#         session.add(movie)
#         session.commit()
#         return item
#
#     def open_spider(self, spider):
#         pass
#
#     def close_spider(self, spider):
#         pass


from datetime import datetime

from sqlalchemy import Column, Integer, String, Text, DateTime

from entity.Movie import Movie
from entity.database import db
from . import Base, loadSession
from sqlalchemy.orm import sessionmaker


# String 需要指定长度参数，否则报错


class MoviescrapyPipeline(object):
    def process_item(self, item, spider):
        movie = Movie()
        movie.title = item['title']
        movie.content = item['content']

        print('数据--%s' % (movie.title))
        print('内容--%s' % (movie.content))


        db.session.add(movie)
        db.session.add(movie)
        db.session.commit()
        return item

    def open_spider(self, spider):
        pass

    def close_spider(self, spider):
        pass
