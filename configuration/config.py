import os
# local db
# ! Environment Variable
DATABASE = 'postgresql://localhost/browser-go'

class BaseConfig:
    """Base configuration."""
    SECRET_KEY = os.getenv('SECRET_KEY')
    DEBUG = False
    BCRYPT_LOG_ROUNDS = 13
    SQLALCHEMY_TRACK_MODIFICATIONS = False

class DevelopmentConfig(BaseConfig):
    """Development configuration."""
    DEBUG = True
    BCRYPT_LOG_ROUNDS = 4
    SQLALCHEMY_DATABASE_URI = DATABASE
    PORT = 5000


class TestingConfig(BaseConfig):
    """Testing configuration."""
    DEBUG = True
    TESTING = True
    BCRYPT_LOG_ROUNDS = 4
    SQLALCHEMY_DATABASE_URI = DATABASE
    PRESERVE_CONTEXT_ON_EXCEPTION = False


class ProductionConfig(BaseConfig):
    """Production configuration."""
    SECRET_KEY = ''
    DEBUG = False
    SQLALCHEMY_DATABASE_URI = 'postgresql:///'
