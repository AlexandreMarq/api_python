# Imports
from mysql.connector import connect
from BD.banco import connection


def consultar(id):
    cursor = connection.cursor()
    sql = f"""SELECT Modelo.id_modelo_antigo
                    , EA.id_equivalente_antigo
                    , P.modelo
                    , descricao_modelo_antigo
                    , modelo_antigo
                    , observacao_modelo_antigo
                    , Foto.link_foto
            FROM modelo_antigo Modelo
            INNER JOIN foto Foto ON Foto.id_foto = Modelo.id_foto
            LEFT JOIN equivalente_antigo EA ON EA.id_modelo_antigo = Modelo.id_modelo_antigo
            LEFT JOIN produto P ON P.id_produto = EA.id_produto 
            WHERE Modelo.id_modelo_antigo = {id};

           """
    cursor.execute(sql)
    row = cursor.fetchall()
    lista_id = []
    lista_modelo = []

    for i in range(len(row)):
        if row[i][1] == row[i][1]:
            lista_id.append(row[i][1])
    for j in range(len(row)):
        if row[j][2] == row[j][2]:
            lista_modelo.append(row[j][2])

    if row is None:
        return None
    connection.commit()
    return({
        "id_modelo_antigo": row[0][0],
        "id_equivalente_antigo": lista_id,
        "modelo": lista_modelo,
        "descricao_modelo_antigo": row[0][3],
        "modelo_antigo": row[0][4],
        "observacao_modelo_antigo": row[0][5],
        "foto": row[0][6]
    })