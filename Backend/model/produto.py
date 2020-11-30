# Class que representa o modelo no bancoclass Manual:

class Produto:
    def __init__(self, descricao_completa, descricao_reduzida, link_codigo_pedido,
                 link_dimensoes, link_esquema_ligacao, link_exemplo_ligacao,
                 link_site, link_tabela_alarmes, link_tabela_parametros, modelo,
                 status, id_alimentacao, id_aplicacao, id_aplicacao_navegacao,
                 id_categoria, id_categoria_venda, id_certificado,
                 id_foto, id_funcao, id_manual, id_montagem):

        self.descricao_completa = descricao_completa
        self.descricao_reduzida = descricao_reduzida
        self.link_codigo_pedido = link_codigo_pedido
        self.link_dimensoes = link_dimensoes
        self.link_esquema_ligacao = link_esquema_ligacao
        self.link_exemplo_ligacao = link_exemplo_ligacao
        self.link_site = link_site
        self.link_tabela_alarmes = link_tabela_alarmes
        self.link_tabela_parametros = link_tabela_parametros
        self.modelo = modelo
        self.status = status
        self.id_alimentacao = id_alimentacao
        self.id_aplicacao = id_aplicacao
        self.id_aplicacao_navegacao = id_aplicacao_navegacao
        self.id_categoria = id_categoria
        self.id_categoria_venda = id_categoria_venda
        self.id_certificado = id_certificado
        self.id_foto = id_foto
        self.id_funcao = id_funcao
        self.id_manual = id_manual
        self.id_montagem = id_montagem

    def atualizar(self, dados):
        try:
            descricao_completa = dados["descricao_completa"]
            descricao_reduzida = dados["descricao_reduzida"]
            link_codigo_pedido = dados['link_codigo_pedido']
            link_dimensoes = dados["link_dimensoes"]
            link_esquema_ligacao = dados["link_esquema_ligacao"]
            link_exemplo_ligacao = dados["link_exemplo_ligacao"]
            link_site = dados["link_site"]
            link_tabela_alarmes = dados["link_tabela_alarmes"]
            link_tabela_parametros = dados["link_tabela_parametros"]
            modelo = dados["modelo"]
            status = dados["status"]

            id_alimentacao = dados["id_alimentacao"]
            id_aplicacao = dados["id_aplicacao"]
            id_aplicacao_navegacao = dados["id_aplicacao_navegacao"]
            id_categoria = dados["id_categoria"]
            id_categoria_venda = dados["id_categoria_venda"]
            id_certificado = dados["id_certificado"]
            id_foto = dados["id_foto"]
            id_funcao = dados["id_funcao"]
            id_manual = dados["id_manual"]
            id_montagem = dados["id_montagem"]

            self.descricao_completa = descricao_completa,
            self.descricao_reduzida = descricao_reduzida,
            self.link_codigo_pedido = link_codigo_pedido,
            self.link_dimensoes = link_dimensoes,
            self.link_esquema_ligacao = link_esquema_ligacao,
            self.link_exemplo_ligacao = link_exemplo_ligacao,
            self.link_site = link_site,
            self.link_tabela_alarmes = link_tabela_alarmes,
            self.link_tabela_parametros = link_tabela_parametros,
            self.modelo = modelo,
            self.status = status,
            self.id_alimentacao = id_alimentacao,
            self.id_aplicacao = id_aplicacao,
            self.id_aplicacao_navegacao = id_aplicacao_navegacao,
            self.id_categoria = id_categoria,
            self.id_categoria_venda = id_categoria_venda,
            self.id_certificado = id_certificado,
            self.id_foto = id_foto,
            self.id_funcao = id_funcao,
            self.id_manual = id_manual,
            self.id_montagem = id_montagem

            return self
        except Exception as e:
            print("Problema ao criar novo Produto!")
            print(e)

    def __dict__(self):
        d = dict()

        d["descricao_completa"] = self.descricao_completa
        d["descricao_reduzida"] = self.descricao_reduzida
        d['link_codigo_pedido'] = self.link_codigo_pedido
        d["link_dimensoes"] = self.link_dimensoes
        d["link_esquema_ligacao"] = self.link_esquema_ligacao
        d["link_exemplo_ligacao"] = self.link_exemplo_ligacao
        d["link_site"] = self.link_site
        d["link_tabela_alarmes"] = self.link_tabela_alarmes
        d["link_tabela_parametros"] = self.link_tabela_parametros
        d["modelo"] = self.modelo
        d["status"] = self.status

        d["id_alimentacao"] = self.id_alimentacao
        d["id_aplicacao"] = self.id_aplicacao
        d["id_aplicacao_navegacao"] = self.id_aplicacao_navegacao
        d["id_categoria"] = self.id_categoria
        d["id_categoria_venda"] = self.id_categoria_venda
        d["id_certificado"] = self.id_certificado
        d["id_foto"] = self.id_foto
        d["id_funcao"] = self.id_funcao
        d["id_manual"] = self.id_manual
        d["id_montagem"] = self.id_montagem

        return d

    @staticmethod
    def criar(dados):
        try:
            descricao_completa = dados["descricao_completa"]
            descricao_reduzida = dados["descricao_reduzida"]
            link_codigo_pedido = dados['link_codigo_pedido']
            link_dimensoes = dados["link_dimensoes"]
            link_esquema_ligacao = dados["link_esquema_ligacao"]
            link_exemplo_ligacao = dados["link_exemplo_ligacao"]
            link_site = dados["link_site"]
            link_tabela_alarmes = dados["link_tabela_alarmes"]
            link_tabela_parametros = dados["link_tabela_parametros"]
            modelo = dados["modelo"]
            status = dados["status"]

            id_alimentacao = dados["id_alimentacao"]
            id_aplicacao = dados["id_aplicacao"]
            id_aplicacao_navegacao = dados["id_aplicacao_navegacao"]
            id_categoria = dados["id_categoria"]
            id_categoria_venda = dados["id_categoria_venda"]
            id_certificado = dados["id_certificado"]
            id_foto = dados["id_foto"]
            id_funcao = dados["id_funcao"]
            id_manual = dados["id_manual"]
            id_montagem = dados["id_montagem"]

            return Produto(descricao_completa=descricao_completa, descricao_reduzida=descricao_reduzida,
                           link_codigo_pedido=link_codigo_pedido, link_dimensoes=link_dimensoes,
                           link_esquema_ligacao=link_esquema_ligacao, link_exemplo_ligacao=link_exemplo_ligacao,
                           link_site=link_site, link_tabela_alarmes=link_tabela_alarmes,
                           link_tabela_parametros=link_tabela_parametros, modelo=modelo,
                           status=status, id_alimentacao=id_alimentacao, id_aplicacao=id_aplicacao,
                           id_aplicacao_navegacao=id_aplicacao_navegacao, id_categoria=id_categoria,
                           id_categoria_venda=id_categoria_venda, id_certificado=id_certificado,
                           id_foto=id_foto, id_funcao=id_funcao,
                           id_manual=id_manual, id_montagem=id_montagem)
        except Exception as e:
            print("Problema ao criar novo Produto!")
            print(e)
