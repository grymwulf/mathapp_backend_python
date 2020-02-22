import json
from flask import request

from . import root_blueprint

@root_blueprint.route('/results', methods=['GET'])
def getAllResults():
    return "get all results"