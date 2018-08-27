from datetime import datetime

from flask import Flask, render_template, jsonify
from flask_marshmallow import Marshmallow
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql+pymysql://dba:111@45.78.9.17:3306/wq_01?charset=utf8'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = True

db = SQLAlchemy(app)
ma = Marshmallow(app)


class Movie(db.Model):
    __tablename__ = 'movie'
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(255), unique=True)
    content = db.Column(db.Text)
    createTime = db.Column(db.DateTime, nullable=False, default=datetime.utcnow)
    updateTime = db.Column(db.DateTime, nullable=False, default=datetime.utcnow)


#
# class MovieSchema(ma.Schema):
#     class Meta:
#         fields = ('id', 'title', 'content', 'createTime', 'updateTime')


class MovieSchema(ma.ModelSchema):
    class Meta:
        model = Movie


# https://www.cnblogs.com/alima/p/5734992.html
# https://wing324.github.io/2017/02/25/%E4%BD%BF%E7%94%A8flask-sqlalchemy%E7%8E%A9%E8%BD%ACMySQL/
# https://www.rithmschool.com/courses/flask-fundamentals/using-jsonify
@app.route('/')
def index():
    return render_template('index.html')


@app.route('/admin')
def admin():
    return render_template('admin.html')


@app.route('/movies')
def movies():
    #
    # result = {
    #     'items': pagination.items,
    #     'total': pagination.total
    # }
    # return jsonify(result)

    # return jsonify([
    #     {'id': movie.id, 'content': movie.content, 'title': movie.title}
    #     for movie in Movie.query.all()
    # ])
    pagination = Movie.query.order_by(Movie.createTime.desc()).paginate(page=1, per_page=10, error_out=True)

    result = {
        'items':  MovieSchema(many=True).dumps(pagination.items),
        'total': pagination.total
    }

    return jsonify(result)


if __name__ == '__main__':
    app.run(debug=True)
