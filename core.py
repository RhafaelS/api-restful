from flask import Flask, jsonify, request
from flask_basicauth import BasicAuth


app = Flask(__name__)

app.config['BASIC_AUTH_USERNAME'] = 'mwork'
app.config['BASIC_AUTH_PASSWORD'] = 'totalerp'

basic_auth = BasicAuth(app)

class nota:
    def __init__(self, cnpj, serie, numero):
        self.cnpj = cnpj
        self.serie = serie
        self.numero = numero


nfealt = nota('11836535000113', '001', '10045')

montajson = {'cnpj': nfealt.cnpj, 'serie': nfealt.serie, 'numero': nfealt.numero}


@app.route('/', methods = ['POST', 'GET'])
@basic_auth.required
def index():
    return jsonify(montajson)


app.run(debug=True)