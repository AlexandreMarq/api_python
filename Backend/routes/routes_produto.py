from flask import Blueprint, jsonify, request
from services.produto_services import \
    listar as service_listar_produto, \
    localizar as service_localiza_produto, \
    criar as service_criar_produto, \
    atualizar as service_atualiza_produto, \
    remover as service_remover_produto, \
    localizar_modelo as service_localiza_modelo

coel_produto = Blueprint('coel_produto', __name__)


@coel_produto.route('/produto')
def listar_produto():
    lista = service_listar_produto()
    return jsonify(lista)


@coel_produto.route('/produto', methods=['POST'])
def cadastrar_produto():
    novo_produto = request.get_json()

    if 'modelo' not in novo_produto or 'status' not in novo_produto:
        return jsonify({'erro': 'produto faltando dados'}), 400

    lista = service_listar_produto()
    for i in range(len(lista)):
        if novo_produto["modelo"] == lista[i]["modelo"]:
            return jsonify({'erro': 'produto ja existe'}), 400

    produto = service_criar_produto(novo_produto)
    if produto is None:
        return jsonify({'erro': 'produto ja existe'}), 400
    return jsonify(produto)


@coel_produto.route('/produto/<int:id>', methods=['GET'])
def localizar_produto(id):
    produto = service_localiza_produto(id)
    if produto is not None:
        return jsonify(produto)
    return jsonify({'erro': 'produto nao encontrado'}), 400


@coel_produto.route('/produto/<modelo>', methods=['GET'])
def localizar_produto_modelo(modelo):
    produto = service_localiza_modelo(modelo)
    if produto is not None:
        return jsonify(produto)
    return jsonify({'erro': 'modelo nao encontrado'}), 400


@coel_produto.route('/produto/<int:id>', methods=['PUT'])
def alterar_produto(id):
    produto_data = request.get_json()

    atualizado = service_atualiza_produto(id, produto_data["descricao_completa"],
                                          produto_data["descricao_reduzida"],
                                          produto_data["link_codigo_pedido"],
                                          produto_data["link_dimensoes"],
                                          produto_data["link_esquema_ligacao"],
                                          produto_data["link_exemplo_ligacao"],
                                          produto_data["link_site"],
                                          produto_data["link_tabela_alarmes"],
                                          produto_data["link_tabela_parametros"],
                                          produto_data["modelo"],
                                          produto_data["status"],
                                          produto_data["id_alimentacao"],
                                          produto_data["id_aplicacao"],
                                          produto_data["id_aplicacao_navegacao"],
                                          produto_data["id_categoria"],
                                          produto_data["id_categoria_venda"],
                                          produto_data["id_certificado"],
                                          produto_data["id_foto"],
                                          produto_data["id_funcao"],
                                          produto_data["id_manual"],
                                          produto_data["id_montagem"])
    if atualizado is not None:
        return jsonify(atualizado), 200
    return jsonify({'erro': 'produto nao encontrado'}), 400


@ coel_produto.route('/produto/<int:id>', methods=['DELETE'])
def remover_produto(id):
    removido = service_remover_produto(id)
    if removido == 1:
        return jsonify({"Sucesso": "removido com sucesso"}), 202
    return jsonify({'erro': 'produto nao encontrado'}), 400
