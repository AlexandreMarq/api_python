from flask import Blueprint, jsonify, request
from services.montagem_services import \
    listar as service_listar_montagem, \
    localizar as service_localiza_montagem

coel_montagem = Blueprint('coel_montagem', __name__)

@coel_montagem.route('/montagem')
def listar_montagem():
    lista = service_listar_montagem()
    return jsonify(lista)

@coel_montagem.route('/montagem/<id>', methods=['GET'])
def localizar_montagem(id):
    montagem = service_localiza_montagem(id)
    if montagem is not None:
        return jsonify(montagem)
    return jsonify({'erro': 'montagem nao encontrado'}), 400
