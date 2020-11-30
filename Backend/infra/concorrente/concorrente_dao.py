# Imports
from mysql.connector import connect
from BD.banco import connection

# Tabela
model_name = "concorrente"


# Query que lista tudo da tabela
def listar():
    cursor = connection.cursor()
    cursor.execute(f"SELECT * FROM {model_name};")
    rows = cursor.fetchall()
    registros = []
    for (id_concorrente, codigo_concorrente, descricao_concorrente,
            empresa_concorrente, observacao_concorrente) in rows:
        registros.append(
            {"id_concorrente": id_concorrente,
             "codigo_concorrente": codigo_concorrente,
             "descricao_concorrente": descricao_concorrente,
             "empresa_concorrente": empresa_concorrente,
             "observacao_concorrente": observacao_concorrente})
    
    cursor.close()
    return registros


# Query que consulta por ID a tabela
def consultar(id):
    cursor = connection.cursor()
    cursor.execute(
        f"SELECT * FROM {model_name} WHERE id_concorrente = %s", (id,))
    row = cursor.fetchone()
    if row is None:
        return None
    return ({"id_concorrente": row[0],
             "codigo_concorrente": row[1],
             "descricao_concorrente": row[2],
             "empresa_concorrente": row[3],
             "observacao_concorrente": row[4]})


def consultar_concorrente(concorrente):
    cursor = connection.cursor()
    cursor.execute(
        f"SELECT * FROM {model_name} WHERE codigo_concorrente LIKE %s", (concorrente + '%',))
    rows = cursor.fetchall()
    registros = []
    for (id_concorrente, codigo_concorrente, descricao_concorrente,
            empresa_concorrente, observacao_concorrente) in rows:
        registros.append(
            {"id_concorrente": id_concorrente,
             "codigo_concorrente": codigo_concorrente,
             "descricao_concorrente": descricao_concorrente,
             "empresa_concorrente": empresa_concorrente,
             "observacao_concorrente": observacao_concorrente})
    return registros


# Query que insere os dados na tabela
def cadastrar(concorrente):
    cursor = connection.cursor()
    sql = f"INSERT INTO {model_name} (codigo_concorrente, descricao_concorrente, empresa_concorrente, observacao_concorrente) VALUES (%s, %s, %s, %s)"
    cursor.execute(sql, (concorrente.codigo_concorrente,
                         concorrente.descricao_concorrente,
                         concorrente.empresa_concorrente,
                         concorrente.observacao_concorrente))
    connection.commit()
    return concorrente.__dict__()


# Query que altera os dados na tabela
def alterar(concorrente):
    cursor = connection.cursor()
    sql = f"UPDATE {model_name} SET codigo_concorrente = %s, descricao_concorrente = %s, empresa_concorrente = %s, observacao_concorrente = %s WHERE id_concorrente = %s"
    cursor.execute(sql, (concorrente["codigo_concorrente"],
                         concorrente["descricao_concorrente"],
                         concorrente["empresa_concorrente"],
                         concorrente["observacao_concorrente"],
                         concorrente["id"]))
    connection.commit()


# Query que remove os dados na tabela
def remover(concorrente):
    cursor = connection.cursor()
    sql = f"DELETE FROM {model_name} WHERE id_concorrente = {concorrente['id_concorrente']}"
    cursor.execute(sql)
    connection.commit()
