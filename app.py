import math

from flask import Flask, abort, request
from werkzeug.routing import FloatConverter as BaseFloatConverter


class FloatConverter(BaseFloatConverter):
    regex = r'^[-+]?\d+(?:\.\d+)?'


app = Flask(__name__)
app.url_map.converters['float'] = FloatConverter


@app.route('/sum/<float:a>/<float:b>')
def sum(a, b):
    return str(a + b)


@app.route('/sub/<float:a>/<float:b>')
def sub(a, b):
    return str(a - b)


@app.route('/mul/<float:a>/<float:b>')
def mul(a, b):
    return str(a * b)


@app.route('/div/<float:a>/<float:b>')
def div(a, b):
    if b == 0:
        return abort(400, 'divide by zero')
    return str(a / b)


@app.route('/div_int/<float:a>/<float:b>')
def div_int(a, b):
    if b == 0:
        return abort(400, 'divide by zero')
    return str(a // b)


@app.route('/mod/<float:a>/<float:b>')
def mod(a, b):
    if b == 0:
        return abort(400, 'divide by zero')
    return str(a % b)


@app.route('/sqrt/<float:a>')
def sqrt(a):
    if a < 0:
        return abort(400, 'sqrt cannot be negative')
    return str(math.sqrt(a))


@app.route('/sin/<float:a>')
def sin(a):
    if request.args.get('mode') == 'degrees':
        a = math.radians(a)
    return str(math.sin(a))


@app.route('/cos/<float:a>')
def cos(a):
    if request.args.get('mode') == 'degrees':
        a = math.radians(a)
    return str(math.cos(a))


@app.route('/tan/<float:a>')
def tan(a):
    if request.args.get('mode') == 'degrees':
        a = math.radians(a)
    return str(math.tan(a))


@app.route('/sqr/<float:a>/<float:b>')
def power(a, b):
    return str(math.pow(a, b))


if __name__ == '__main__':
    app.run(host='0.0.0.0', debug=True, port=1001)
