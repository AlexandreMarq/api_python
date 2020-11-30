from flask import Blueprint, jsonify, request
from services.equivalente_antigo_services import \
    listar as service_listar_equivalente, \
    criar as service_criar_equivalente, \
    localizar as service_localiza_antigo, \
    remover as service_remover

coel_equivalente_antigo = Blueprint('coel_equivalente_antigo', __name__)

@coel_equivalente_antigo.route('/equivalente_antigo')
def listar_equivalente_antigo():
    lista = service_listar_equivalente()
    return jsonify(lista)


@coel_equivalente_antigo.route('/equivalente_antigo', methods=['POST'])
def cadastrar_equivalente_antigo():
    novo_equivalente_antigo = request.get_json()

    if 'id_modelo_antigo' not in novo_equivalente_antigo or 'id_produto' not in novo_equivalente_antigo:
        return jsonify({'erro': 'equivalente_antigo sem id_modelo_antigo ou id_produto'}), 400

    equivalente_antigo = service_criar_equivalente(novo_equivalente_antigo)
    if equivalente_antigo is None:
        return jsonify({'erro': 'equivalente_antigo ja existe'}), 400
    return jsonify(equivalente_antigo)


@coel_equivalente_antigo.route('/equivalente_antigo/<int:id>', methods=['GET'])
def localizar_equivalente_antigo_id(id):
    equivalente_antigo = service_localiza_antigo(id)
    if equivalente_antigo is not None:
        return jsonify(equivalente_antigo)
    return jsonify({'erro': 'equivalente_antigo nao encontrado'}), 400


@coel_equivalente_antigo.route('/equivalente_antigo/<deletavel>', methods=['DELETE'])
def remover_equivalente_antigo(deletavel):
    removido = service_remover(deletavel)
    if removido == 1:
        return jsonify({"Sucesso":"removido com sucesso"}), 202
    return jsonify({'erro': 'concorrente nao encontrado'}), 400
