# encoding: utf-8

# dialect+driver://username:password@host:port/database
DIALECT = 'mysql'
DRIVER = 'mysqldb'
USERNAME = 'root'
PASSWORD = 'liulong'
HOST = '127.0.0.1'
PORT = '3306'
DATABASE = 'test'

SQLALCHEMY_DATABASE_URI = "{}+{}://{}:{}@{}:{}/{}?charset=utf-8".format(DIALECT, DRIVER, USERNAME, PASSWORD,
                                                                        HOST, PORT, DATABASE)
SQLALCHEMY_TRACK_MODIFICATIONS = True

