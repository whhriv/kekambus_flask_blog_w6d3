from flask import Blueprint


api = Blueprint('api', __name__, url_prefix='/api')

@api.route('/test')
def test():
    return 'this is a test'

from . import routes