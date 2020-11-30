# Imports de modolus internos da aplicação
from infra.montagem.montagem_dao import \
    listar as dao_listar, \
    consultar as dao_consultar


# Função que lista montagem
def listar():
    return [montagem for montagem in dao_listar()]


# Função que localiza montagem por ID
def localizar(id):
    montagem = dao_consultar(id)
    if montagem is None:
        return None
    return montagem
