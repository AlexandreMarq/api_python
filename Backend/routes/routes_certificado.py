from flask import Blueprint, jsonify, request
from services.certificado_services import \
    listar as service_listar_certificado, \
    localizar as service_localiza_certificado

coel_certificado = Blueprint('coel_certificado', __name__)

@coel_certificado.route('/certificado')
def listar_certificado():
    lista = service_listar_certificado()
    return jsonify(lista)

@coel_certificado.route('/certificado/<id>', methods=['GET'])
def localizar_certificado(id):
    certificado = service_localiza_certificado(id)
    if certificado is not None:
        return jsonify(certificado)
    return jsonify({'erro': 'certificado nao encontrado'}), 400
