# Imports de modolus internos da aplicação
from infra.foto.foto_dao import \
    listar as dao_listar, \
    consultar as dao_consultar

# Função que lista foto
def listar():
    return [foto for foto in dao_listar()]


# Função que localizar foto ID
def localizar(id):
    foto = dao_consultar(id)
    if foto is None:
        return None
    return foto
