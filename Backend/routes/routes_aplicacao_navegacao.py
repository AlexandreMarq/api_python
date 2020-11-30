from flask import Blueprint, jsonify, request
from services.aplicacao_navegacao_services import \
    listar as service_listar_navegacao, \
    localizar as service_localiza_navegacao

coel_navegacao = Blueprint('coel_navegacao', __name__)

@coel_navegacao.route('/navegacao')
def listar_navegacao():
    lista = service_listar_navegacao()
    return jsonify(lista)

@coel_navegacao.route('/navegacao/<id>', methods=['GET'])
def localizar_navegacao(id):
    navegacao = service_localiza_navegacao(id)
    if navegacao is not None:
        return jsonify(navegacao)
    return jsonify({'erro': 'navegacao nao encontrado'}), 400
