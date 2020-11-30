# Imports
from mysql.connector import connect
from BD.banco import connection

# Tabela
model_name = "funcao"


# Query que lista tudo da tabela
def listar():
    cursor = connection.cursor()
    cursor.execute(f"SELECT * FROM {model_name};")
    rows = cursor.fetchall()
    registros = []
    for (id_funcao, funcao) in rows:
        registros.append(
            {"id_funcao": id_funcao, "funcao": funcao})
    
    cursor.close()
    return registros

# Query que consulta por ID a tabela
def consultar(id):
    cursor = connection.cursor()
    cursor.execute(
        f"SELECT * FROM {model_name} WHERE id_funcao = %s", (id,))
    row = cursor.fetchone()
    if row is None:
        return None
    
    cursor.close()
    return ({"id_funcao": row[0], "funcao": row[1]})
