# Imports de modolus internos
from infra.visualizar.produto_visualizar_dao import consultar

# Função que localiza produto por ID
def localizar(id):
    produto = consultar(id)
    if produto is None:
        return None
    return produto

