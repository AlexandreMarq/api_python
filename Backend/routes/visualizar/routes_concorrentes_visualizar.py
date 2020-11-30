from flask import Blueprint, jsonify, request
from services.visualizar.concorrente_visualizar_services import localizar_concorente

coel_concorrente_visualizar = Blueprint('coel_concorrente_visualizar', __name__)


@coel_concorrente_visualizar.route('/concorrente_visualizar/<int:id>', methods=['GET'])
def localizar_concorente_join(id):
    concorrente = localizar_concorente(id)
    if concorrente is not None:
        return jsonify(concorrente)
    return jsonify({'erro': 'concorrente nao encontrado'}), 400
