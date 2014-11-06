from flask import Flask
from flask.ext.pymongo import PyMongo
import os
import ConfigParser
from logging.handlers import RotatingFileHandler


#Create PyMongo object
mongo = PyMongo()


def create_app():
    '''Create the Flask app.
    '''
    #Create the Flask app
    app = Flask(__name__)

    #Load configurations
    load_config(app)

    #Configure logginig
    configure_logging(app)

    # Register URL rules.
    register_url_rules(app)

    #Initialize the app for use with PyMongo
    mongo.init_app(app, config_prefix="MONGO")

    return app


def load_config(app):
    ''' Reads the config file and loads configuration properties
     into the Flask app.
    :param app: The Flask app object.
    '''

    #Get the path to the application directory, that's where the config file resides.
    par_dir = os.path.join(__file__, os.pardir)
    par_dir_abs_path = os.path.abspath(par_dir)
    app_dir = os.path.dirname(par_dir_abs_path)

    # Get configuration file
    # http://flask.pocoo.org/docs/config/
    config = ConfigParser.RawConfigParser()
    config_filepath = app_dir + '/config.cfg'
    config.read(config_filepath)

    #Set up configuration properties
    app.config['SERVER_PORT'] = config.get('Application', 'SERVER_PORT')
    app.config['MONGO_DBNAME'] = config.get('Mongo', 'DB_NAME')

    # Logging path might be relative or starts from the root.
    # If it's relative then be sure to prepend the path with the application's root directory path.
    log_path = config.get('Logging', 'PATH')
    if log_path.startswith('/'):
        app.config['LOG_PATH'] = log_path
    else:
        app.config['LOG_PATH'] = app_dir + '/' + log_path

    app.config['LOG_LEVEL'] = config.get('Logging', 'LEVEL').upper()

    # Set the secret key, keep this really secret. We need this for session manager.
    # Check out sectopm "How to generate good secret keys" in http://flask.pocoo.org/docs/quickstart/
    app.secret_key = config.get('Application', 'SECRET_KEY')


def configure_logging(app):
    ''' Configure the app's logging.
     param app: The Flask app object
    '''

    log_path = app.config['LOG_PATH']
    log_level = app.config['LOG_LEVEL']

    # If path directory doesn't exist, create it.
    log_dir = os.path.dirname(log_path)
    if not os.path.exists(log_dir):
        os.makedirs(log_dir)

    # Create and register the log file handler.
    log_handler = RotatingFileHandler(log_path, maxBytes=250000, backupCount=5)
    log_handler.setLevel(log_level)
    app.logger.addHandler(log_handler)

    app.logger.info('Logging to: %s', log_path)


# Import forms
from views.index import Index


def register_url_rules(app):
    ''' Register the URL rules using pluggable class-based views
    '''

    # Index page form.
    app.add_url_rule('/', view_func=Index.as_view('index'))
