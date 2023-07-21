import os


class Config(object):
    SECRET_KEY = os.environ.get('SECRET_KEY') or 'local-dev-key'
    DEBUG = False
    TESTING = False
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    SQLALCHEMY_DATABASE_URI = os.environ.get('PROD_DATABASE_URL')


class DevelopmentConfig(Config):
    DEBUG = True
    SQLALCHEMY_DATABASE_URI = os.environ.get('DEV_DATABASE_URL')


class ProductionConfig(Config):
    DEBUG = False


configuration = {
    'development': DevelopmentConfig,
    'production': ProductionConfig
}