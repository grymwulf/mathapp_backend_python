from flask import Blueprint

root_blueprint = Blueprint('root', __name__)

from . import results
from . import students
from . import teachers
from . import tests