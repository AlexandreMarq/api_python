# Imports de modolus internos da aplicação
from infra.funcao.funcao_dao import \
    listar as dao_listar, \
    consultar as dao_consultar

# Função que listar Funcao
def listar():
    return [funcao for funcao in dao_listar()]


# Função que localizar Funcao por ID
def localizar(id):
    funcao = dao_consultar(id)
    if funcao is None:
        return None
    return funcao
