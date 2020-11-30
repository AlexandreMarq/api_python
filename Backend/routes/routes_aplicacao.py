from flask import Blueprint, jsonify, request
from services.aplicacao_services import \
    listar as service_listar_aplicacao, \
    localizar as service_localiza_aplicacao

coel_aplicacao = Blueprint('coel_aplicacao', __name__)

@coel_aplicacao.route('/aplicacao')
def listar_aplicacao():
    lista = service_listar_aplicacao()
    return jsonify(lista)

@coel_aplicacao.route('/aplicacao/<id>', methods=['GET'])
def localizar_aplicacao(id):
    aplicacao = service_localiza_aplicacao(id)
    if aplicacao is not None:
        return jsonify(aplicacao)
    return jsonify({'erro': 'aplicacao nao encontrado'}), 400
