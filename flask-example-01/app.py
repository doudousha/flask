from flask import Flask , render_template
from data import Articles

app = Flask(__name__)

@app.route('/')
def index():
    return "hell world"

@app.route('/home')
def home():
    return render_template('index.html')

@app.route('/articles')
def articles():
    articles = Articles()
    return render_template('articles.html',articles = articles)

@app.route('/article/<string:id>/')
def article(id):
    articles = Articles()
    return render_template('article.html',id = id)

class RegisterForm(Form):
    name = StringField('Name',[validators.Length(min=1,max=50)])
    username = StringField('Username',[validators.Length(min=4,max=25)])
    email = StringField('Email',[validators.Length(min=6,max=50)])
    password = PasswordField('Password',[
        validators.DataRequired(),
        validators.EqualTo('confirm',message ='Passwords do not match')
    ])
    confirm = PasswordField('Confirm Password')



@app.route('/register',methods=['GET','POST'])
def register():
    form = RegisterForm(request.form)
    if request.method == 'POST' and  form.validate()

    return render_template('register.html',form = form)

if __name__ == '__main__':
    # debug = true 可以打开热部署，修改文件后服务器自动重启
    app.run('0.0.0.0',debug = True)