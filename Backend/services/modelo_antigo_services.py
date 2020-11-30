# Imports de modolus internos da aplicação
from infra.modelo_antigo.modelo_antigo_dao import \
    listar as dao_listar_modelo_antigo, \
    consultar as dao_consultar_modelo_antigo, \
    cadastrar as dao_cadastrar_modelo_antigo, \
    alterar as dao_alterar_modelo_antigo, \
    remover as dao_remover_modelo_antigo, \
    consultar_modelo as dao_consultar_modelo
from model.modelo_antigo import Modelo_antigo


# Função que lista Modelo antigo
def listar():
    return [modelo_antigo for modelo_antigo in dao_listar_modelo_antigo()]


# Função que localiza Modelo antigo por ID
def localizar(id):
    modelo_antigo = dao_consultar_modelo_antigo(id)
    if modelo_antigo is None:
        return None
    return modelo_antigo


# Função que localiza Modelo antigo por modelo
def localizar_modelo(modelo):
    modelo_antigo = dao_consultar_modelo(modelo)
    if modelo_antigo is None:
        return None
    return modelo_antigo


# Função que cria Modelo antigo
def criar(modelo_antigo_dados):
    modelo_antigo = Modelo_antigo.criar(modelo_antigo_dados)
    return dao_cadastrar_modelo_antigo(modelo_antigo)


# Função que remover Modelo antigo por ID
def remover(id):
    dados_modelo_antigo = localizar(id)
    if dados_modelo_antigo is None:
        return 0
    dao_remover_modelo_antigo(dados_modelo_antigo)
    return 1

# Função que atualiza os dados de Modelo antigo
def atualizar(id, descricao_modelo_antigo, modelo_antigo,
              observacao_modelo_antigo, id_foto):
    modelo_antigo = {"descricao_modelo_antigo": descricao_modelo_antigo, "modelo_antigo": modelo_antigo,
                     "observacao_modelo_antigo": observacao_modelo_antigo, "id_foto": id_foto,
                     "id": id}

    dao_alterar_modelo_antigo(modelo_antigo)
    return localizar(id)
