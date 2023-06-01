# Import the os module, which allows you to interact with the underlying operating system in several different ways
import os


# Define the Config class for Flask application configurations
class Config:
    # SECRET_KEY used for creating secure tokens, such as session tokens
    SECRET_KEY = os.environ.get('SECRET_KEY')

    # Database configuration
    # SQLALCHEMY_DATABASE_URI is the location of the database
    SQLALCHEMY_DATABASE_URI = os.environ.get('SQLALCHEMY_DATABASE_URI')

    # Email configuration
    # Config for the Mail Server to send emails from the application
    MAIL_SERVER = 'smtp.googlemail.com'
    MAIL_PORT = 587
    MAIL_USE_TLS = True
    # MAIL_USERNAME and MAIL_PASSWORD are fetched from environment variables
    MAIL_USERNAME = os.environ.get('EMAIL_USER')
    MAIL_PASSWORD = os.environ.get('EMAIL_PASS')
