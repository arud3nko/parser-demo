from utils import module
from flask import render_template, request, abort, Flask
import uuid

app = Flask(__name__)
app.secret_key = 'top_secret_key_anti_hack_100lvl'


def random_symbols(length=10):
    return str(uuid.uuid4()).split('-')[0]


@app.route('/')
def index():
    variable = random_symbols()
    return render_template('main.html', variable=variable)


@app.route('/<var>', methods=['POST', 'GET'])
def process(var):

    if request.method == 'POST':
        address = request.form['address']
        mail = request.form['mail']
        return render_template('process.html', address=address, mail=mail)
    return abort(404)


@app.route('/yield', methods=['POST', 'GET'])
def stream():
    if request.method == 'POST':

        address = request.form['address']
        mail = request.form['mail']
        return app.response_class(module.inner(address, mail), mimetype='text/html')

    return abort(404)


app.run(host='0.0.0.0', port='5000')

