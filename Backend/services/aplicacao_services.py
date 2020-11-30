# Imports de modolus internos da aplicação
from infra.aplicacao.aplicacao_dao import \
    listar as dao_listar, \
    consultar as dao_consultar

# Função que lista Aplicacao
def listar():
    return [aplicacao for aplicacao in dao_listar()]


# Função que localiza Aplicacao por ID
def localizar(id):
    aplicacao = dao_consultar(id)
    if aplicacao is None:
        return None
    return aplicacao
