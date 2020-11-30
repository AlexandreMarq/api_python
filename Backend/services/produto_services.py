# Imports de modolus internos da aplicação
from infra.produto.produto_dao import \
    listar as dao_listar_produto, \
    consultar as dao_consultar_produto, \
    cadastrar as dao_cadastrar_produto, \
    alterar as dao_alterar_produto, \
    remover as dao_remover_produto, \
    consultar_modelo as dao_consultar_modelo
from model.produto import Produto


# Função que lista Produto
def listar():
    return [produto for produto in dao_listar_produto()]


# Função que localiza produto por ID
def localizar(id):
    produto = dao_consultar_produto(id)
    if produto is None:
        return None
    return produto


# Função que localiza produto por ID
def localizar_modelo(modelo):
    produto = dao_consultar_modelo(modelo)
    if produto is None:
        return None
    return produto


# Função que cria produto
def criar(produto_dados):
    produto = Produto.criar(produto_dados)
    return dao_cadastrar_produto(produto)


# Função que remover Modelo antigo por ID
def remover(id):
    dados_produto = localizar(id)
    if dados_produto is None:
        return 0
    dao_remover_produto(dados_produto)
    return 1


# Função que atualiza os dados de Modelo antigo
def atualizar(id, descricao_completa, descricao_reduzida, link_codigo_pedido,
              link_dimensoes, link_esquema_ligacao, link_exemplo_ligacao,
              link_site, link_tabela_alarmes, link_tabela_parametros, modelo,
              status, id_alimentacao, id_aplicacao, id_aplicacao_navegacao,
              id_categoria, id_categoria_venda, id_certificado,
              id_foto, id_funcao, id_manual, id_montagem):

    produto = {"descricao_completa": descricao_completa, "descricao_reduzida": descricao_reduzida,
               "link_codigo_pedido": link_codigo_pedido, "link_dimensoes": link_dimensoes,
               "link_esquema_ligacao": link_esquema_ligacao, "link_exemplo_ligacao": link_exemplo_ligacao,
               "link_site": link_site, "link_tabela_alarmes": link_tabela_alarmes,
               "link_tabela_parametros": link_tabela_parametros, "modelo": modelo, "status": status,
               "id_alimentacao": id_alimentacao, "id_aplicacao": id_aplicacao,
               "id_aplicacao_navegacao": id_aplicacao_navegacao, "id_categoria": id_categoria,
               "id_categoria_venda": id_categoria_venda, "id_certificado": id_certificado,
               "id_foto": id_foto, "id_funcao": id_funcao,
               "id_manual": id_manual, "id_montagem": id_montagem,
               "id": id}

    dao_alterar_produto(produto)
    return localizar(id)
