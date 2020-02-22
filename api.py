import flask
import os

# Get environment variables
os.environ['']

app = flask.Flask(__name__)
app.config["DEBUG"] = True
@app.route