from flask import Blueprint, jsonify, request
from services.modelo_antigo_services import \
    listar as service_listar_modelo_antigo, \
    localizar as service_localiza_modelo_antigo, \
    criar as service_criar_modelo_antigo, \
    atualizar as service_atualiza_modelo_antigo, \
    remover as service_remover_modelo_antigo, \
    localizar_modelo as service_localizar_modelo

coel_modelo_antigo = Blueprint('coel_modelo_antigo', __name__)


@coel_modelo_antigo.route('/modelo_antigo')
def listar_modelo_antigo():
    lista = service_listar_modelo_antigo()
    return jsonify(lista)


@coel_modelo_antigo.route('/modelo_antigo', methods=['POST'])
def cadastrar_modelo_antigo():
    novo_modelo_antigo = request.get_json()

    if 'modelo_antigo' not in novo_modelo_antigo or 'descricao_modelo_antigo' not in novo_modelo_antigo:
        return jsonify({'erro': 'modelo_antigo faltando dados'}), 400

    lista = service_listar_modelo_antigo()
    for i in range(len(lista)):
        if novo_modelo_antigo["modelo_antigo"] == lista[i]["modelo_antigo"]:
            return jsonify({'erro': 'modelo_antigo ja existe'}), 400

    modelo_antigo = service_criar_modelo_antigo(novo_modelo_antigo)
    if modelo_antigo is None:
        return jsonify({'erro': 'modelo_antigo ja existe'}), 400
    return jsonify(modelo_antigo)


@coel_modelo_antigo.route('/modelo_antigo/<int:id>', methods=['GET'])
def localizar_modelo_antigo(id):
    modelo_antigo = service_localiza_modelo_antigo(id)
    if modelo_antigo is not None:
        return jsonify(modelo_antigo)
    return jsonify({'erro': 'modelo_antigo nao encontrado'}), 400


@coel_modelo_antigo.route('/modelo_antigo/<modelo>', methods=['GET'])
def localizar_modelo(modelo):
    modelo_antigo = service_localizar_modelo(modelo)
    if modelo_antigo is not None:
        return jsonify(modelo_antigo)
    return jsonify({'erro': 'modelo_antigo nao encontrado'}), 400


@coel_modelo_antigo.route('/modelo_antigo/<int:id>', methods=['PUT'])
def alterar_modelo_antigo(id):
    modelo_antigo_data = request.get_json()

    if 'descricao_modelo_antigo' not in modelo_antigo_data:
        return jsonify({'erro': 'modelo_antigo sem descricao_modelo_antigo'}), 400

    if 'modelo_antigo' not in modelo_antigo_data:
        return jsonify({'erro': 'modelo_antigo sem modelo_antigo'}), 400

    if 'observacao_modelo_antigo' not in modelo_antigo_data:
        return jsonify({'erro': 'modelo_antigo sem observacao_modelo_antigo'}), 400

    if 'id_foto' not in modelo_antigo_data:
        return jsonify({'erro': 'modelo_antigo sem id_foto'}), 400

    atualizado = service_atualiza_modelo_antigo(id, modelo_antigo_data['descricao_modelo_antigo'],
                                                modelo_antigo_data["modelo_antigo"],
                                                modelo_antigo_data["observacao_modelo_antigo"],
                                                modelo_antigo_data["id_foto"])
    if atualizado is not None:
        return jsonify(atualizado), 200
    return jsonify({'erro': 'modelo_antigo nao encontrado'}), 400


@coel_modelo_antigo.route('/modelo_antigo/<int:id>', methods=['DELETE'])
def remover_modelo_antigo(id):
    removido = service_remover_modelo_antigo(id)
    if removido == 1:
        return jsonify({"Sucesso": "removido com sucesso"}), 202
    return jsonify({'erro': 'modelo_antigo nao encontrado'}), 400
