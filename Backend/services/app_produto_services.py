# Imports de modolus internos da aplicação
from infra.produto.app_produto_dao import \
    listar as dao_listar_produto, \
    consultar as dao_consultar_produto


# Função que lista Produto
def listar():
    return [produto for produto in dao_listar_produto()]


# Função que localiza produto por ID
def localizar(id):
    produto = dao_consultar_produto(id)
    if produto is None:
        return None
    return produto
