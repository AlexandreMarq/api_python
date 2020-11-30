from flask import Blueprint, jsonify, request
from services.visualizar.produto_visualizar_services import localizar

coel_produto_visualizar = Blueprint('coel_produto_visualizar', __name__)

@coel_produto_visualizar.route('/produto_visualizar/<int:id>', methods=['GET'])
def localizar_produto(id):
    produto = localizar(id)
    if produto is not None:
        return jsonify(produto)
    return jsonify({'erro': 'produto nao encontrado'}), 400


    