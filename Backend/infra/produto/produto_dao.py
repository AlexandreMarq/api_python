# Imports
from mysql.connector import connect
from BD.banco import connection

# Tabela
model_name = "produto"


# Query que lista tudo da tabela
def listar():
    cursor = connection.cursor()
    cursor.execute(f"SELECT * FROM {model_name};")
    rows = cursor.fetchall()
    registros = []
    for (id_produto, descricao_completa, descricao_reduzida, link_codigo_pedido,
         link_dimensoes, link_esquema_ligacao, link_exemplo_ligacao,
         link_site, link_tabela_alarmes, link_tabela_parametros, modelo, status,
         id_alimentacao, id_aplicacao, id_aplicacao_navegacao,
         id_categoria, id_categoria_venda, id_certificado,
         id_foto, id_funcao, id_manual, id_montagem) in rows:
        registros.append(
            {"id_produto": id_produto,
             "descricao_completa": descricao_completa,
             "descricao_reduzida": descricao_reduzida,
             "link_codigo_pedido": link_codigo_pedido,
             "link_dimensoes": link_dimensoes,
             "link_esquema_ligacao": link_esquema_ligacao,
             "link_exemplo_ligacao": link_exemplo_ligacao,
             "link_site": link_site,
             "link_tabela_alarmes": link_tabela_alarmes,
             "link_tabela_parametros": link_tabela_parametros,
             "modelo": modelo,
             "status": status,
             "id_alimentacao": id_alimentacao,
             "id_aplicacao": id_aplicacao,
             "id_aplicacao_navegacao": id_aplicacao_navegacao,
             "id_categoria": id_categoria,
             "id_categoria_venda": id_categoria_venda,
             "id_certificado": id_certificado,
             "id_foto": id_foto,
             "id_funcao": id_funcao,
             "id_manual": id_manual,
             "id_montagem": id_montagem})
    return registros


# Query que consulta por ID a tabela
def consultar(id):
    cursor = connection.cursor()
    cursor.execute(
        f"SELECT * FROM {model_name} WHERE id_produto = %s", (id,))
    row = cursor.fetchone()
    if row is None:
        return None
    return ({"id_produto": row[0],
             "descricao_completa": row[1],
             "descricao_reduzida": row[2],
             "link_codigo_pedido": row[3],
             "link_dimensoes": row[4],
             "link_esquema_ligacao": row[5],
             "link_exemplo_ligacao": row[6],
             "link_site": row[7],
             "link_tabela_alarmes": row[8],
             "link_tabela_parametros": row[9],
             "modelo": row[10],
             "status": row[11],
             "id_alimentacao": row[12],
             "id_aplicacao": row[13],
             "id_aplicacao_navegacao": row[14],
             "id_categoria": row[15],
             "id_categoria_venda": row[16],
             "id_certificado": row[17],
             "id_foto": row[18],
             "id_funcao": row[19],
             "id_manual": row[20],
             "id_montagem": row[21]})


# Query que consulta por ID a tabela
def consultar_modelo(modelo):
    cursor = connection.cursor()
    cursor.execute(
        f"SELECT * FROM {model_name} WHERE modelo like %s", (modelo + '%',))
    rows = cursor.fetchall()
    registros = []
    for (id_produto, descricao_completa, descricao_reduzida, link_codigo_pedido,
            link_dimensoes, link_esquema_ligacao, link_exemplo_ligacao,
            link_site, link_tabela_alarmes, link_tabela_parametros, modelo, status,
            id_alimentacao, id_aplicacao, id_aplicacao_navegacao,
            id_categoria, id_categoria_venda, id_certificado,
            id_foto, id_funcao, id_manual, id_montagem) in rows:
        registros.append(
            {"id_produto": id_produto,
             "descricao_completa": descricao_completa,
             "descricao_reduzida": descricao_reduzida,
             "link_codigo_pedido": link_codigo_pedido,
             "link_dimensoes": link_dimensoes,
             "link_esquema_ligacao": link_esquema_ligacao,
             "link_exemplo_ligacao": link_exemplo_ligacao,
             "link_site": link_site,
             "link_tabela_alarmes": link_tabela_alarmes,
             "link_tabela_parametros": link_tabela_parametros,
             "modelo": modelo,
             "status": status,
             "id_alimentacao": id_alimentacao,
             "id_aplicacao": id_aplicacao,
             "id_aplicacao_navegacao": id_aplicacao_navegacao,
             "id_categoria": id_categoria,
             "id_categoria_venda": id_categoria_venda,
             "id_certificado": id_certificado,
             "id_foto": id_foto,
             "id_funcao": id_funcao,
             "id_manual": id_manual,
             "id_montagem": id_montagem})
    return registros


# Query que insere os dados na tabela
def cadastrar(produto):
    cursor = connection.cursor()
    sql = f"INSERT INTO {model_name} (descricao_completa, descricao_reduzida, link_codigo_pedido, link_dimensoes, link_esquema_ligacao, link_exemplo_ligacao, link_site, link_tabela_alarmes, link_tabela_parametros, modelo, status, id_alimentacao, id_aplicacao, id_aplicacao_navegacao, id_categoria, id_categoria_venda, id_certificado, id_foto, id_funcao, id_manual, id_montagem) VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)"
    cursor.execute(sql, (produto.descricao_completa,
                         produto.descricao_reduzida,
                         produto.link_codigo_pedido,
                         produto.link_dimensoes,
                         produto.link_esquema_ligacao,
                         produto.link_exemplo_ligacao,
                         produto.link_site,
                         produto.link_tabela_alarmes,
                         produto.link_tabela_parametros,
                         produto.modelo,
                         produto.status,
                         produto.id_alimentacao,
                         produto.id_aplicacao,
                         produto.id_aplicacao_navegacao,
                         produto.id_categoria,
                         produto.id_categoria_venda,
                         produto.id_certificado,
                         produto.id_foto,
                         produto.id_funcao,
                         produto.id_manual,
                         produto.id_montagem))
    connection.commit()
    return produto.__dict__()


# Query que altera os dados na tabela
def alterar(produto):
    cursor = connection.cursor()
    sql = f"UPDATE {model_name} SET descricao_completa = %s, descricao_reduzida = %s, link_codigo_pedido = %s, link_dimensoes = %s, link_esquema_ligacao = %s, link_exemplo_ligacao = %s, link_site = %s, link_tabela_alarmes = %s, link_tabela_parametros = %s, modelo = %s, status = %s, id_alimentacao = %s, id_aplicacao = %s, id_aplicacao_navegacao = %s, id_categoria = %s, id_categoria_venda = %s, id_certificado = %s, id_foto = %s, id_funcao = %s, id_manual = %s, id_montagem = %s WHERE id_produto = %s"
    cursor.execute(sql, (produto["descricao_completa"],
                         produto["descricao_reduzida"],
                         produto["link_codigo_pedido"],
                         produto["link_dimensoes"],
                         produto["link_esquema_ligacao"],
                         produto["link_exemplo_ligacao"],
                         produto["link_site"],
                         produto["link_tabela_alarmes"],
                         produto["link_tabela_parametros"],
                         produto["modelo"],
                         produto["status"],
                         produto["id_alimentacao"],
                         produto["id_aplicacao"],
                         produto["id_aplicacao_navegacao"],
                         produto["id_categoria"],
                         produto["id_categoria_venda"],
                         produto["id_certificado"],
                         produto["id_foto"],
                         produto["id_funcao"],
                         produto["id_manual"],
                         produto['id_montagem'],
                         produto["id"]))
    connection.commit()


# Query que remove os dados na tabela
def remover(produto):
    cursor = connection.cursor()
    sql = f"DELETE FROM {model_name} WHERE id_produto = {produto['id_produto']}"
    cursor.execute(sql)
    connection.commit()
