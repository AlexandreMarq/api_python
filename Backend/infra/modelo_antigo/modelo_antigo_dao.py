# Imports
from mysql.connector import connect
from BD.banco import connection

# Tabela
model_name = "modelo_antigo"


# Query que lista tudo da tabela
def listar():
    cursor = connection.cursor()
    cursor.execute(f"SELECT * FROM {model_name};")
    rows = cursor.fetchall()
    registros = []
    for (id_modelo_antigo, descricao_modelo_antigo,
         modelo_antigo, observacao_modelo_antigo, id_foto) in rows:
        registros.append(
            {"id_modelo_antigo": id_modelo_antigo,
             "descricao_modelo_antigo": descricao_modelo_antigo,
             "modelo_antigo": modelo_antigo,
             "observacao_modelo_antigo": observacao_modelo_antigo,
             "id_foto": id_foto})
    
    cursor.close()
    return registros


# Query que consulta por ID a tabela
def consultar(id):
    cursor = connection.cursor()
    cursor.execute(
        f"SELECT * FROM {model_name} WHERE id_modelo_antigo = %s", (id,))
    row = cursor.fetchone()
    if row is None:
        return None
    
    cursor.close()
    return ({"id_modelo_antigo": row[0],
             "descricao_modelo_antigo": row[1],
             "modelo_antigo": row[2],
             "observacao_modelo_antigo": row[3],
             "id_foto": row[4]})


# Query que consulta por ID a tabela
def consultar_modelo(modelo):
    cursor = connection.cursor()
    cursor.execute(
        f"SELECT * FROM {model_name} WHERE modelo_antigo LIKE %s", (modelo + '%',))
    rows = cursor.fetchall()
    registros = []
    for (id_modelo_antigo, descricao_modelo_antigo,
         modelo_antigo, observacao_modelo_antigo, id_foto) in rows:
        registros.append(
            {"id_modelo_antigo": id_modelo_antigo,
             "descricao_modelo_antigo": descricao_modelo_antigo,
             "modelo_antigo": modelo_antigo,
             "observacao_modelo_antigo": observacao_modelo_antigo,
             "id_foto": id_foto})
    
    cursor.close()
    return registros


# Query que insere os dados na tabela
def cadastrar(modelo_antigo):
    cursor = connection.cursor()
    sql = f"INSERT INTO {model_name} (descricao_modelo_antigo, modelo_antigo, observacao_modelo_antigo, id_foto) VALUES (%s, %s, %s, %s)"
    cursor.execute(sql, (modelo_antigo.descricao_modelo_antigo,
                         modelo_antigo.modelo_antigo,
                         modelo_antigo.observacao_modelo_antigo,
                         modelo_antigo.id_foto))
    
    cursor.close()
    connection.commit()
    return modelo_antigo.__dict__()


# Query que altera os dados na tabela
def alterar(modelo_antigo):
    cursor = connection.cursor()
    sql = f"UPDATE {model_name} SET descricao_modelo_antigo = %s, modelo_antigo = %s, observacao_modelo_antigo = %s, id_foto = %s WHERE id_modelo_antigo = %s"
    cursor.execute(sql, (modelo_antigo["descricao_modelo_antigo"],
                         modelo_antigo["modelo_antigo"],
                         modelo_antigo["observacao_modelo_antigo"],
                         modelo_antigo["id_foto"], modelo_antigo["id"]))
    
    cursor.close()
    connection.commit()

# Query que remove os dados na tabela


def remover(modelo_antigo):
    cursor = connection.cursor()
    sql = f"DELETE FROM {model_name} WHERE id_modelo_antigo = {modelo_antigo['id_modelo_antigo']}"
    cursor.execute(sql)

    cursor.close()
    connection.commit()
