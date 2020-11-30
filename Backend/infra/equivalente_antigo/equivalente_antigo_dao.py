# Imports
from mysql.connector import connect
from BD.banco import connection


# Tabela
model_name = "equivalente_antigo"


# Query que lista tudo da tabela
def listar():
    cursor = connection.cursor()
    cursor.execute(f"SELECT * FROM {model_name};")
    rows = cursor.fetchall()
    registros = []
    for (id_equivalente_antigo, id_modelo_antigo, id_produto) in rows:
        registros.append(
            {"id_equivalente_antigo": id_equivalente_antigo,
             "id_modelo_antigo": id_modelo_antigo,
             "id_produto": id_produto})
    cursor.close()
    return registros


# Query que consulta por ID a tabela
def consultar(id):
    cursor = connection.cursor()
    cursor.execute(
        f"SELECT * FROM {model_name} WHERE id_equivalente_antigo = %s", (id,))
    row = cursor.fetchone()
    if row is None:
        return None
    cursor.close()
    return ({"id_equivalente_antigo": row[0],
             "id_modelo_antigo": row[1],
             "id_produto": row[2]})


# Query que insere os dados na tabela
def cadastrar(equivalente_antigo):
    cursor = connection.cursor()
    sql = f"INSERT INTO {model_name} (id_modelo_antigo, id_produto) VALUES (%s, %s)"
    cursor.execute(sql, (equivalente_antigo.id_modelo_antigo, equivalente_antigo.id_produto))
    
    cursor.close()
    connection.commit()
    
    return equivalente_antigo.__dict__()


# Query que remove os dados na tabela
def remover(deletavel):
    cursor = connection.cursor()
    sql = f"DELETE FROM {model_name} WHERE id_equivalente_antigo in ({deletavel})"
    cursor.execute(sql)
    
    cursor.close()
    connection.commit()