from os import environ
from dotenv import load_dotenv

load_dotenv()


class Config:

    # Flask configuration
    FLASK_APP = environ.get('FLASK_APP')
    FLASK_ENV = environ.get('FLASK_ENV')

    SECRET_KEY = environ.get('SECRET_KEY')

    TESTING = environ.get('TESTING')

    REPOSITORY = environ.get('REPOSITORY')

    ALCHEMY_URI = environ.get("ALCHEMY_URI")
