import flask
import os
from dotenv import load_dotenv
from models import db

# Load environment variables
load_dotenv()

# Get environment variables
appPort = os.environ['PORT']
dbHostName = os.environ['RDS_HOSTNAME']
dbName = os.environ['RDS_DB_NAME']
dbUser = os.environ['RDS_USERNAME']
dbPassword = os.environ['RDS_PASSWORD']
dbPort = os.environ['RDS_PORT']
dbDialect = os.environ['DB_DIALECT']
appEnvironment = os.environ['APP_ENVIRONMENT']

# Configure app

app = flask.Flask(__name__, instance_relative_config=True)

if appEnvironment == 'dev':
    app.config["DEBUG"] = True

app.config["SQLALCHEMY_DATABASE_URI"] = (dbDialect + '://' 
    + dbUser + ':' + dbPassword 
    + '@' + dbHostName + '/' + dbName )


# Register our routes - doing both the api spec and base as a redirect
from routes import root_blueprint
app.register_blueprint(root_blueprint, url_prefix='/api/v1/')
app.register_blueprint(root_blueprint)


# Run app
if __name__ == '__main__':
    print("Port = " + appPort)
    print("Database URI " + app.config["SQLALCHEMY_DATABASE_URI"])
    app.run(port=appPort)