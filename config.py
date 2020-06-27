import os

SECRET_KEY = "#d#JCqTTW\nilK\\7m\x0bp#\tj~#H"


if os.environ.get('DATABASE_URL') is None:
    basedir = os.path.abspath(os.path.dirname(__file__))
    SQLALCHEMY_DATABASE_URI = 'sqlite:///' + os.path.join(basedir, 'app.db')
    FB_APP_ID = 626175137996713
else:
    SQLALCHEMY_DATABASE_URI = os.environ['DATABASE_URL']
    FB_APP_ID = 2875937649201270

basedir = os.path.abspath(os.path.dirname(__file__))
SQLALCHEMY_DATABASE_URI = 'sqlite:///' + os.path.join(basedir, 'app.db')
