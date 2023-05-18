class Config(object):
    DEBUG = False
    SERVER_NAME='localhost. :2000'
    TESTING=False
    SQLALCHEMY_DATABASE_URI='postgresql://postgres:admin@localhost/programs'
class Test(Config):
    TESTING=False
    SERVER_NAME='test:5000'
    DEBUG=True
    SQLALCHEMY_DATABASE_URI='postgresql://postgres:admin@localhost/programs'
class Production(Config):
    TESTING=False
    SERVER_NAME='production:5000'
    SQLALCHEMY_DATABASE_URI='postgresql://postgres:admin@localhost/programs'
    DEBUG=False
class Razrab(Config):
    TESTING=False
    SERVER_NAME='razrab:5000'
    DEBUG=True