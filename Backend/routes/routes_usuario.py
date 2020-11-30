from flask import Blueprint, jsonify, request
from services.usuario_services import \
    listar as service_listar_usuario, \
    localizar as service_localiza_usuario, \
    criar as service_criar_usuario

coel_usuario = Blueprint('coel_usuario', __name__)

@coel_usuario.route('/usuario')
def listar_usuario():
    lista = service_listar_usuario()
    return jsonify(lista)


@coel_usuario.route('/usuario', methods=['POST'])
def cadastrar_usuario():
    novo_usuario = request.get_json()

    if 'login' not in novo_usuario or 'senha' not in novo_usuario:
        return jsonify({'erro': 'usuario sem login ou senha'}), 400

    lista = service_listar_usuario()
    for i in range(len(lista)):
        if novo_usuario["login"] == lista[i]["login"]:
            return jsonify({'erro': 'usuario ja existe'}), 400

    usuario = service_criar_usuario(novo_usuario)
    if usuario is None:
        return jsonify({'erro': 'usuario ja existe'}), 400
    return jsonify(usuario)


@coel_usuario.route('/usuario/<login>', methods=['GET'])
def localizar_usuario(login):
    usuario = service_localiza_usuario(login)
    if usuario is not None:
        return jsonify(usuario)
    return jsonify({'erro': 'usuario nao encontrado'}), 400
