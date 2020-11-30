from flask import Blueprint, jsonify, request
from services.funcao_services import \
    listar as service_listar_funcao, \
    localizar as service_localiza_funcao

coel_funcao = Blueprint('coel_funcao', __name__)

@coel_funcao.route('/funcao')
def listar_funcao():
    lista = service_listar_funcao()
    return jsonify(lista)

@coel_funcao.route('/funcao/<id>', methods=['GET'])
def localizar_funcao(id):
    funcao = service_localiza_funcao(id)
    if funcao is not None:
        return jsonify(funcao)
    return jsonify({'erro': 'funcao nao encontrado'}), 400
