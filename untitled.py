# encoding: utf-8

from flask import Flask, render_template
from models import Article, User
from exts import db


app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql+pymysql://root:liulong@localhost/test'
app.config['SQLALCHEMY_COMMIT_TEARDOWN'] = True
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = True

db.init_app(app)


@app.route('/user')
def hello():
    # 想要添加一篇文章，因为文章必须依赖用户再存在，所以首先添加一个用户
    # user1 = User(username='zhangsan')
    # db.session.add(user1)
    # db.session.commit()
    # article1 = Article(title='aaa', content='bbb')
    # article1.author = User.query.filter(User.id == 1).first()
    # db.session.add(article1)
    # db.session.commit()

    # 我要找文章标题为aaa的这个作者
    # article = Article.query.filter(Article.title == 'aaa').first()
    # print(article.author.username)
    # article1 = Article(title='111', content='222', auth_id=1)
    # db.session.add(article1)
    # db.session.commit()
    # 要找到用户写过的所有文章
    # user = User.query.filter(User.username == 'lisi').first()
    # result = user.articles
    # for article in result:
    #     print('='*10)
    #     print(article.title)
    return u'你好！'


@app.route('/')
def hello_world():
    # 增
    # article1 = Article(title='AAA', content='BBB')
    # db.session.add(article1)
    # db.session.commit()
    # 查
    # result = Article.query.filter(Article.title == 'AAA').first()
    # print(result.title)
    # print(result.content)
    #改
    # article1 = Article.query.filter(Article.title == 'AAA').first()
    # article1.title = 'new title'
    # db.session.commit()
    # 删
    # article1 = Article.query.filter(Article.content == 'BBB').first()
    # db.session.delete(article1)
    # db.session.commit()
    return 'Hello world'


@app.route('/article/<id>')
def article(id):
    return u'您请求的参数是: %s' % id


@app.route('/list/')
def my_list():
    return 'list'


if __name__ == '__main__':
    app.run(debug=True)
