from flask import Blueprint, jsonify, request
from services.equivalente_concorrente_services import \
    listar as service_listar_equivalente, \
    criar as service_criar_equivalente, \
    localizar as service_localiza_equivalente, \
    remover as service_remover

coel_equivalente_concorrente = Blueprint('coel_equivalente_concorrente', __name__)

@coel_equivalente_concorrente.route('/equivalente_concorrente')
def listar_equivalente_concorrente():
    lista = service_listar_equivalente()
    return jsonify(lista)


@coel_equivalente_concorrente.route('/equivalente_concorrente', methods=['POST'])
def cadastrar_equivalente_concorrente():
    novo_equivalente_concorrente = request.get_json()

    if 'id_concorrente' not in novo_equivalente_concorrente or 'id_produto' not in novo_equivalente_concorrente:
        return jsonify({'erro': 'equivalente_concorrente sem id_concorrente ou id_produto'}), 400

    equivalente_concorrente = service_criar_equivalente(novo_equivalente_concorrente)
    if equivalente_concorrente is None:
        return jsonify({'erro': 'equivalente_concorrente ja existe'}), 400
    return jsonify(equivalente_concorrente)


@coel_equivalente_concorrente.route('/equivalente_concorrente/<int:id>', methods=['GET'])
def localizar_equivalente_concorrente_id(id):
    equivalente_concorrente = service_localiza_equivalente(id)
    if equivalente_concorrente is not None:
        return jsonify(equivalente_concorrente)
    return jsonify({'erro': 'equivalente_concorrente nao encontrado'}), 400


@coel_equivalente_concorrente.route('/equivalente_concorrente/<deletavel>', methods=['DELETE'])
def remover_equivalente_concorrente(deletavel):
    removido = service_remover(deletavel)
    if removido == 1:
        return jsonify({"Sucesso":"removido com sucesso"}), 202
    return jsonify({'erro': 'concorrente nao encontrado'}), 400
