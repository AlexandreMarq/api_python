# Imports de modolus internos da aplicação
from infra.alimentacao.alimentacao_dao import \
    listar as dao_listar, \
    consultar as dao_consultar

# Função que lista Aimentacao
def listar():
    return [alimentacao for alimentacao in dao_listar()]


# Função que localiza Aimentacao por ID
def localizar(id):
    alimentacao = dao_consultar(id)
    if alimentacao is None:
        return None
    return alimentacao
