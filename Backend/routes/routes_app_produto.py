from flask import Blueprint, jsonify, request
from services.app_produto_services import \
    listar as service_listar_produto, \
    localizar as service_localiza_produto

coel_app_produto = Blueprint('coel_app_produto', __name__)


@coel_app_produto.route('/app_produto')
def listar_produto():
    lista = service_listar_produto()
    return jsonify(lista)


@coel_app_produto.route('/app_produto/<int:id>', methods=['GET'])
def localizar_produto(id):
    produto = service_localiza_produto(id)
    if produto is not None:
        return jsonify(produto)
    return jsonify({'erro': 'produto nao encontrado'}), 400
