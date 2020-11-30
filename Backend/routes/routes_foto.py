from flask import Blueprint, jsonify, request
from services.foto_services import \
    listar as service_listar_foto, \
    localizar as service_localiza_foto

coel_foto = Blueprint('coel_foto', __name__)

@coel_foto.route('/foto')
def listar_foto():
    lista = service_listar_foto()
    return jsonify(lista)

@coel_foto.route('/foto/<id>', methods=['GET'])
def localizar_foto(id):
    foto = service_localiza_foto(id)
    if foto is not None:
        return jsonify(foto)
    return jsonify({'erro': 'foto nao encontrado'}), 400
