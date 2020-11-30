# Imports de modolus internos da aplicação
from infra.categoria.categoria_dao import \
    listar as dao_listar, \
    consultar as dao_consultar

# Função que lista Categoria
def listar():
    return [categoria for categoria in dao_listar()]

# Função que localiza Categoria por ID
def localizar(id):
    categoria = dao_consultar(id)
    if categoria is None:
        return None
    return categoria
