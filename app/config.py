class Configuration(object):
    DEBUG = True
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    SQLALCHEMY_DATABASE_URI = 'mysql+mysqlconnector://batman:1@localhost/flask_test'
    SECRET_KEY = 'batman in the jungle%%%'
    ###FLASK SECURITY
    """
    install bcrypt
        take a good salt
    """
    SECURITY_PASSWORD_SALT = 'salt'
    SECURITY_PASSWORD_HASH = 'sha512_crypt'