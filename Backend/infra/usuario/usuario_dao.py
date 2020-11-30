# Imports
from mysql.connector import connect
from BD.banco import connection

# Tabela
model_name = "usuario"


# Query que lista tudo da tabela
def listar():
    cursor = connection.cursor()
    cursor.execute(f"SELECT * FROM {model_name};")
    rows = cursor.fetchall()
    registros = []
    for (id_usuario, login, senha) in rows:
        registros.append(
            {"id_usuario": id_usuario, "login": login, "senha": senha})
    
    cursor.close()
    return registros

# Query que consulta por ID a tabela
def consultar(login):
    cursor = connection.cursor()
    cursor.execute(
        f"SELECT * FROM {model_name} WHERE login = %s", (login,))
    row = cursor.fetchone()
    if row is None:
        return None
    
    cursor.close()
    return ({"id_usuario": row[0], "login": row[1], "senha": row[2]})


# Query que insere os dados na tabela
def cadastrar(usuario):
    cursor = connection.cursor()
    sql = f"INSERT INTO {model_name} (login, senha) VALUES (%s, %s)"
    cursor.execute(sql, (usuario.login, usuario.senha))
    cursor.close()
    connection.commit()
    return usuario.__dict__()
