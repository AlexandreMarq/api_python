# Imports de modolus internos da aplicação
from infra.usuario.usuario_dao import \
    listar as dao_listar, \
    consultar as dao_consultar, \
    cadastrar as dao_cadastrar

from model.usuario import Usuario


# Função que lista os usuarios
def listar():
    return [usuario for usuario in dao_listar()]


# Função que localiza o usuario por login
def localizar(login):
    usuario = dao_consultar(login)
    if usuario is None:
        return None
    return usuario


# Função que cria Usuario
def criar(usuario_dados):
    usuario = Usuario.criar(usuario_dados)
    return dao_cadastrar(usuario)
