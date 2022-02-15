import os


class Config:

    QUOTE_API_BASE_URL ='http://quotes.stormconsultancy.co.uk/random.json'
    SECRET_KEY = 'barbz'
    # SQLALCHEMY_DATABASE_URI = 'postgresql+psycopg2://postgres:password@localhost/blogs'
    SQLALCHEMY_DATABASE_URI = ('postgresql://xbytshqrcnejxz:073bbb312ba84b40bcc07df260858ddbf3bfa9b7b9a73d529b59b067cbeb4ccb@ec2-52-207-74-100.compute-1.amazonaws.com:5432/ddhs9q1bi4ab55')
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    UPLOADED_PHOTOS_DEST ='app/static/photos'

    #  email configurations
    MAIL_SERVER = 'smtp.googlemail.com'
    MAIL_PORT = 587
    MAIL_USE_TLS = True
    MAIL_USERNAME = os.environ.get("MAIL_USERNAME")
    MAIL_PASSWORD = os.environ.get("MAIL_PASSWORD")

    # simple mde  configurations
    SIMPLEMDE_JS_IIFE = True
    SIMPLEMDE_USE_CDN = True

class ProdConfig(Config):
    SQLALCHEMY_DATABASE_URI = ('postgresql://xbytshqrcnejxz:073bbb312ba84b40bcc07df260858ddbf3bfa9b7b9a73d529b59b067cbeb4ccb@ec2-52-207-74-100.compute-1.amazonaws.com:5432/ddhs9q1bi4ab55')


class DevConfig(Config):
    # SQLALCHEMY__URI = 'postgresql+psycopg2://postgres:password@localhost/blogs'
    SQLALCHEMY_DATABASE_URI = ('postgresql://xbytshqrcnejxz:073bbb312ba84b40bcc07df260858ddbf3bfa9b7b9a73d529b59b067cbeb4ccb@ec2-52-207-74-100.compute-1.amazonaws.com:5432/ddhs9q1bi4ab55')
    DEBUG = True

    
config_options = {
'development':DevConfig,
'production':ProdConfig,
}