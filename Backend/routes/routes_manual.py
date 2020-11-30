from flask import Blueprint, jsonify, request
from services.manual_services import \
    listar as service_listar_manual, \
    localizar as service_localiza_manual

coel_manual = Blueprint('coel_manual', __name__)

@coel_manual.route('/manual')
def listar_manual():
    lista = service_listar_manual()
    return jsonify(lista)

@coel_manual.route('/manual/<id>', methods=['GET'])
def localizar_manual(id):
    manual = service_localiza_manual(id)
    if manual is not None:
        return jsonify(manual)
    return jsonify({'erro': 'manual nao encontrado'}), 400
