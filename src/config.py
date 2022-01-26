# /src/config.py

import os
from dotenv import load_dotenv, find_dotenv

load_dotenv(find_dotenv())

class Development(object):
    """
    Development environment configuration
    """
    DEBUG = True
    TESTING = False
    SQLALCHEMY_TRACK_MODIFICATIONS=False
    SQLALCHEMY_DATABASE_URI = "postgres://postgres:123qwe@localhost:5433/softcon"
    JWT_SECRET_KEY = 'gxARdhXpn2R4mN7QzSOWe18X3kW66k'
    

class Production(object):
    """
    Production environment configurations
    """
    DEBUG = False
    TESTING = False
    SQLALCHEMY_TRACK_MODIFICATIONS=False
    SQLALCHEMY_DATABASE_URI ="postgres://postgres:123qwe@localhost:5433/softcon"
    JWT_SECRET_KEY = 'gxARdhXpn2R4mN7QzSOWe18X3kW66k'

class Testing(object):
    """
    Development environment configuration
    """
    TESTING = True
    JWT_SECRET_KEY = 'gxARdhXpn2R4mN7QzSOWe18X3kW66k'
    SQLALCHEMY_DATABASE_URI = "postgres://postgres:123qwe@localhost:5433/softcon"
    SQLALCHEMY_TRACK_MODIFICATIONS=False

app_config = {
    'development': Development,
    'production': Production,
    'testing': Testing
}
