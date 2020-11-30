from flask import Blueprint, jsonify, request
from services.categoria_venda_services import \
    listar as service_listar_categoria_venda, \
    localizar as service_localiza_categoria_venda

coel_categoria_venda = Blueprint('coel_categoria_venda', __name__)


@coel_categoria_venda.route('/categoria_venda')
def listar_categoria_venda():
    lista = service_listar_categoria_venda()
    return jsonify(lista)


@coel_categoria_venda.route('/categoria_venda/<id>', methods=['GET'])
def localizar_categoria_venda(id):
    categoria_venda = service_localiza_categoria_venda(id)
    if categoria_venda is not None:
        return jsonify(categoria_venda)
    return jsonify({'erro': 'categoria_venda nao encontrado'}), 400
