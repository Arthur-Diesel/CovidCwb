from flask import Flask, jsonify, make_response, url_for
from bs4 import BeautifulSoup
from urllib.request import urlopen
from gevent.pywsgi import WSGIServer

app = Flask(__name__)

url = 'https://coronavirus.curitiba.pr.gov.br'

def scrap():
    html = urlopen(url)
    sopa = BeautifulSoup(html, 'lxml')
    data = sopa.find('span', 
    id='cphBodyMaster_lblDataAtualizacao').get_text()
    data = data.split(' ')
    hora = data[4]
    dia = data[2]
    return sopa, hora, dia

@app.get('/favicon.ico')
def favicon():
    response = make_response(url_for('static', filename='favicon.ico'))
    return response, 200

@app.get('/primeira_vacina')
def primeira():
    try:
        sopa, hora, dia = scrap()
        primeira_dose = sopa.find('span', 
        id='cphBodyMaster_ucVacinometro_lblContadorVacinas').get_text()
        response = make_response(jsonify({'mensagem':'sucesso!', 
        'primeira dose':primeira_dose, 'data':dia, 'hora':hora}))
        return response, 200
    except:
        response = make_response(jsonify({'mensagem':'erro!'}))
        return response, 500

@app.get('/segunda_vacina')
def segunda():
    try:
        sopa, hora, dia = scrap()
        segunda_dose = sopa.find('span', 
        id='cphBodyMaster_ucVacinometro_lblContadorSegundaDose').get_text()
        response = make_response(jsonify({'mensagem':'sucesso!', 
        'segunda dose':segunda_dose, 'data':dia, 'hora':hora}))
        return response, 200
    except:
        response = make_response(jsonify({'mensagem':'erro!'}))
        return response, 500


@app.get('/total_vacinas')
def total_vacina():
    try:
        sopa, hora, dia = scrap()
        primeira_dose = sopa.find('span', 
        id='cphBodyMaster_ucVacinometro_lblContadorVacinas').get_text()
        segunda_dose = sopa.find('span', 
        id='cphBodyMaster_ucVacinometro_lblContadorSegundaDose').get_text()
        response = make_response(jsonify({'mensagem':'sucesso!', 
        'primeira dose':primeira_dose, 'segunda dose':segunda_dose, 
        'data':dia, 'hora':hora}))
        return response, 200
    except:
        response = make_response(jsonify({'mensagem':'erro!'}))
        return response, 500

@app.get('/casos_ativos')
def ativos():
    try:
        sopa, hora, dia = scrap()
        casos_ativos = sopa.find('span', 
        id='cphBodyMaster_lblSuspeitos').get_text()
        response = make_response(jsonify({'mensagem':'sucesso!', 
        'casos ativos':casos_ativos, 'data':dia, 'hora':hora}))
        return response, 200
    except:
        response = make_response(jsonify({'mensagem':'erro!'}))
        return response, 500

@app.get('/casos_confirmados')
def confirmados():
    sopa, hora, dia = scrap()
    casos_confirmados = sopa.find('span',
    id='cphBodyMaster_lblConfirmados').get_text()
    response = make_response(jsonify({'mensagem':'sucesso!', 
    'casos confirmados':casos_confirmados, 'data':dia, 'hora':hora}))
    return response, 200

@app.get('/casos_recuperados')
def recuperados():
    try:
        sopa, hora, dia = scrap()
        casos_recuperados = sopa.find('span', 
        id='cphBodyMaster_lblRecuperados').get_text()
        response = make_response(jsonify({'mensagem':'sucesso!', 
        'casos recuperados':casos_recuperados, 'data':dia, 'hora':hora}))
        return response, 200
    except:
        response = make_response(jsonify({'mensagem':'erro!'}))
        return response, 500

@app.get('/casos')
def total_casos():
    try:
        sopa,hora,dia = scrap()
        casos_ativos = sopa.find('span', 
        id='cphBodyMaster_lblSuspeitos').get_text()
        casos_confirmados = sopa.find('span', 
        id='cphBodyMaster_lblConfirmados').get_text()
        casos_recuperados = sopa.find('span', 
        id='cphBodyMaster_lblRecuperados').get_text()
        response = make_response(jsonify({'mensagem':'sucesso!', 
        'casos ativos':casos_ativos, 'casos confirmados':casos_confirmados, 
        'casos recuperados':casos_recuperados, 'data':dia, 'hora':hora}))
        return response, 200
    except:
        response = make_response(jsonify({'mensagem':'erro!'}))
        return response, 500

@app.get('/obitos')
def obitos():
    try:
        sopa, hora, dia = scrap()
        obitos = sopa.find('span', 
        id='cphBodyMaster_lblObitos').get_text()
        response = make_response(jsonify({'mensagem':'sucesso!', 
        'obitos':obitos, 'data':dia, 'hora':hora}))
        return response, 200
    except:
        response = make_response(jsonify({'mensagem':'erro!'}))
        return response, 500

@app.get('/ocupacao_uti')
def ocupacao():
    try:
        sopa, hora, dia = scrap()
        ocupacao_uti = sopa.find('span', 
        id='cphBodyMaster_lblOcupacao').get_text()
        response = make_response(jsonify({'mensagem':'sucesso!', 
        'ocupacao':ocupacao_uti, 'data':dia, 'hora':hora}))
        return response, 200
    except:
        response = make_response(jsonify({'mensagem':'erro!'}))
        return response, 500

@app.get('/leitos_livres')
def livres():
    try:
        sopa, hora, dia = scrap()
        leitos_livres = sopa.find('span', 
        id='cphBodyMaster_lblLeitosLivres').get_text()
        response = make_response(jsonify({'mensagem':'sucesso!', 
        'leitos livres':leitos_livres, 'data':dia, 'hora':hora}))
        return response, 200
    except:
        response = make_response(jsonify({'mensagem':'erro!'}))
        return response, 500

@app.get('/dados')
def total():
    try:
        sopa, hora, dia = scrap()
        primeira_dose = sopa.find('span', 
        id='cphBodyMaster_ucVacinometro_lblContadorVacinas').get_text()
        segunda_dose = sopa.find('span', 
        id='cphBodyMaster_ucVacinometro_lblContadorSegundaDose').get_text()
        casos_ativos = sopa.find('span', 
        id='cphBodyMaster_lblSuspeitos').get_text()
        casos_confirmados = sopa.find('span', 
        id='cphBodyMaster_lblConfirmados').get_text()
        casos_recuperados = sopa.find('span', 
        id='cphBodyMaster_lblRecuperados').get_text()
        obitos = sopa.find('span', 
        id='cphBodyMaster_lblObitos').get_text()
        ocupacao_uti = sopa.find('span', 
        id='cphBodyMaster_lblOcupacao').get_text()
        leitos_livres = sopa.find('span', 
        id='cphBodyMaster_lblLeitosLivres').get_text()

        dados = {
            'primeira dose':primeira_dose,
            'segunda dose':segunda_dose,
            'casos ativos':casos_ativos,
            'casos confirmados':casos_confirmados,
            'casos recuperados':casos_recuperados,
            'obitos':obitos,
            'ocupacao uti':ocupacao_uti,
            'leitos livres':leitos_livres,
            'dia':dia,
            'hora':hora
        }

        response = make_response(jsonify(dados))
        return response, 200

    except:
        response = make_response(jsonify({'mensagem':'erro!'}))
        return response, 500

print(':)')
http_server = WSGIServer(('', 5000), app)
http_server.serve_forever()