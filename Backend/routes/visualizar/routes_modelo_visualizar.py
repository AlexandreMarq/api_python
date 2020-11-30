from flask import Blueprint, jsonify, request
from services.visualizar.modelo_visualizar_services import localizar_modelo

coel_modelo_visualizar = Blueprint('coel_modelo_visualizar', __name__)


@coel_modelo_visualizar.route('/modelo_visualizar/<int:id>', methods=['GET'])
def localizar_modelo_join(id):
    modelo = localizar_modelo(id)
    if modelo is not None:
        return jsonify(modelo)
    return jsonify({'erro': 'modelo nao encontrado'}), 400
