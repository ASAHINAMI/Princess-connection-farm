import json

from flask import Response


class NotFoundError(Response):
    def __init__(self, msg='not found', data=''):
        result = json.dumps(dict(code=404, msg=msg, data=data))
        Response.__init__(self, result, mimetype='application/json')


class BadRequestError(Response):
    def __init__(self, msg='bad request', data=''):
        result = json.dumps(dict(code=400, msg=msg, data=data))
        Response.__init__(self, result, mimetype='application/json')
