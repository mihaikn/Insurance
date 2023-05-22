class Config(object):
    DEBUG = False
    TESTING=False
    SQLALCHEMY_DATABASE_URI='postgresql://postgres:admin@localhost/programs'
class Test(Config):
    TESTING=False
    DEBUG=True
    SQLALCHEMY_DATABASE_URI='postgresql://postgres:admin@localhost/programs'
class Production(Config):
    TESTING=False
    SQLALCHEMY_DATABASE_URI='postgresql://admin:root@127.0.0.1:5431/programms'
    DEBUG=False
class Razrab(Config):
    TESTING=False
    DEBUG=True