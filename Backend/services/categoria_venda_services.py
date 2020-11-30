from infra.categoria_venda.categoria_venda_dao import \
    listar as dao_listar, \
    consultar as dao_consultar

# Função que lista Categoria venda
def listar():
    return [categoria_venda for categoria_venda in dao_listar()]


# Função que localiza Categoria venda por ID
def localizar(id):
    categoria_venda = dao_consultar(id)
    if categoria_venda is None:
        return None
    return categoria_venda
