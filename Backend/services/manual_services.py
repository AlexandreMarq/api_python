# Imports de modolus internos da aplicação
from infra.manual.manual_dao import \
    listar as dao_listar, \
    consultar as dao_consultar

# Função que lista Manual
def listar():
    return [manual for manual in dao_listar()]


# Função que localiza Manual por ID
def localizar(id):
    manual = dao_consultar(id)
    if manual is None:
        return None
    return manual
