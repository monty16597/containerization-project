# config.py
import os

class Config:
    DATABASE_USER = os.getenv('DATABASE_USER', 'postgres')
    DATABASE_PASSWORD = os.getenv('DATABASE_PASSWORD', 'postgres')
    DATABASE_HOST = os.getenv('DATABASE_HOST', 'postgres')
    DATABASE_DB_NAME = os.getenv('DATABASE_DB_NAME', 'postgres')
    SQLALCHEMY_DATABASE_URI = os.getenv('DATABASE_URL', f'postgresql://{DATABASE_USER}:{DATABASE_PASSWORD}@{DATABASE_HOST}/{DATABASE_DB_NAME}')
    SQLALCHEMY_TRACK_MODIFICATIONS = False
