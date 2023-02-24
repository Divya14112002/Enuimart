import os
baseDirectory = os.path.abspath(os.path.dirname(__file__))

class Config():
    DEBUG = False
    SQLITE_DB_DIRECTORY = None
    SQLALCHEMY_DATABASE_URI = None 
    SQLALCHEMY_TRACK_MODIFICATIONS = False 

class LocalDevelopmentConfig(Config):
    DEBUG = True
    SQLITE_DB_DIRECTORY = os.path.join(baseDirectory, '../db_directory')
    SQLALCHEMY_DATABASE_URI = 'sqlite:///' + os.path.join(SQLITE_DB_DIRECTORY, 'eunimart.sqlite3')