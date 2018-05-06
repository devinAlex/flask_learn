# encoding: utf-8

from flask_script import Manager
from untitled import app
from db_script import DBManager

manager = Manager(app)


@manager.command
def runserver():
    print('服务器跑起来了！！！')


manager.add_command('db', DBManager)


if __name__ == '__main__':
    manager.run()