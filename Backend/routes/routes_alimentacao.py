# Imports
from flask import Blueprint, jsonify, request
from services.alimentacao_services import \
    listar as service_listar_alimentacao, \
    localizar as service_localiza_alimentacao

coel_alimentacao = Blueprint('coel_alimentacao', __name__)


@coel_alimentacao.route('/alimentacao')
def listar_alimentacao():
    lista = service_listar_alimentacao()
    return jsonify(lista)


@coel_alimentacao.route('/alimentacao/<id>', methods=['GET'])
def localizar_alimentacao(id):
    alimentacao = service_localiza_alimentacao(id)
    if alimentacao is not None:
        return jsonify(alimentacao)
    return jsonify({'erro': 'alimentacao nao encontrado'}), 400
