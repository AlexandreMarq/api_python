from flask import Blueprint, jsonify, request
from services.categoria_services import \
    listar as service_listar_categoria, \
    localizar as service_localiza_categoria

coel_categoria = Blueprint('coel_categoria', __name__)

@coel_categoria.route('/categoria')
def listar_categoria():
    lista = service_listar_categoria()
    return jsonify(lista)

@coel_categoria.route('/categoria/<id>', methods=['GET'])
def localizar_categoria(id):
    categoria = service_localiza_categoria(id)
    if categoria is not None:
        return jsonify(categoria)
    return jsonify({'erro': 'categoria nao encontrado'}), 400
