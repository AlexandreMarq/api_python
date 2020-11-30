from flask import Blueprint, jsonify, request
from services.concorrente_services import \
    listar as service_listar_concorrente, \
    localizar as service_localiza_concorrente, \
    criar as service_criar_concorrente, \
    atualizar as service_atualiza_concorrente, \
    remover as service_remover_concorrente, \
    localizar_concorrente as service_localizar_concorrente

coel_concorrente = Blueprint('coel_concorrente', __name__)


@coel_concorrente.route('/concorrente')
def listar_concorrente():
    lista = service_listar_concorrente()
    return jsonify(lista)


@coel_concorrente.route('/concorrente', methods=['POST'])
def cadastrar_concorrente():
    novo_concorrente = request.get_json()

    if 'codigo_concorrente' not in novo_concorrente or 'descricao_concorrente' not in novo_concorrente:
        return jsonify({'erro': 'concorrente faltando dados'}), 400

    lista = service_listar_concorrente()
    for i in range(len(lista)):
        if novo_concorrente["codigo_concorrente"] == lista[i]["codigo_concorrente"]:
            return jsonify({'erro': 'concorrente ja existe'}), 400

    concorrente = service_criar_concorrente(novo_concorrente)
    if concorrente is None:
        return jsonify({'erro': 'concorrente ja existe'}), 400
    return jsonify(concorrente)


@coel_concorrente.route('/concorrente/<int:id>', methods=['GET'])
def localizar_concorrente_id(id):
    concorrente = service_localiza_concorrente(id)
    if concorrente is not None:
        return jsonify(concorrente)
    return jsonify({'erro': 'concorrente nao encontrado'}), 400


@coel_concorrente.route('/concorrente/<concorrente>', methods=['GET'])
def localizar_concorrente(concorrente):
    concorrente = service_localizar_concorrente(concorrente)
    if concorrente is not None:
        return jsonify(concorrente)
    return jsonify({'erro': 'concorrente nao encontrado'}), 400


@coel_concorrente.route('/concorrente/<int:id>', methods=['PUT'])
def alterar_concorrente(id):
    concorrente_data = request.get_json()

    if 'codigo_concorrente' not in concorrente_data:
        return jsonify({'erro': 'concorrente sem codigo_concorrente'}), 400

    if 'descricao_concorrente' not in concorrente_data:
        return jsonify({'erro': 'concorrente sem descricao_concorrente'}), 400

    if 'empresa_concorrente' not in concorrente_data:
        return jsonify({'erro': 'concorrente sem empresa_concorrente'}), 400

    if 'observacao_concorrente' not in concorrente_data:
        return jsonify({'erro': 'concorrente sem observacao_concorrente'}), 400

    atualizado = service_atualiza_concorrente(id, concorrente_data['codigo_concorrente'],
                                              concorrente_data["descricao_concorrente"],
                                              concorrente_data["empresa_concorrente"],
                                              concorrente_data["observacao_concorrente"])
    if atualizado is not None:
        return jsonify(atualizado), 200
    return jsonify({'erro': 'concorrente nao encontrado'}), 400


@coel_concorrente.route('/concorrente/<int:id>', methods=['DELETE'])
def remover_concorrente(id):
    removido = service_remover_concorrente(id)
    if removido == 1:
        return jsonify({"Sucesso":"removido com sucesso"}), 202
    return jsonify({'erro': 'concorrente nao encontrado'}), 400
