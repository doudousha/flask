from datetime import datetime
from entity.database import db


class Movie(db.Model):
    __tablename__ = 'movie'
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(255), unique=True)
    content = db.Column(db.Text)
    createTime = db.Column(db.DateTime, nullable=False, default=datetime.utcnow)
    updateTime = db.Column(db.DateTime, nullable=False, default=datetime.utcnow)


    @property
    def serialize(self):
        return {
            'id': self.id,
            'title': self.title,
            'content': self.content,
        }

    def to_dict(self):
        return {c.name: getattr(self, c.name, None) for c in self.__table__.columns}
