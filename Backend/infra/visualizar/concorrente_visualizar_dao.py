# Imports
from mysql.connector import connect
from BD.banco import connection


# traz uma consulta unindo os campos necessarios
def consultar(id):
    cursor = connection.cursor()
    sql = f"""SELECT C.id_concorrente
                    , EC.id_equivalente_concorrente
                    , P.modelo
                    , codigo_concorrente
                    , descricao_concorrente
                    , empresa_concorrente
                    , observacao_concorrente
                FROM concorrente C
                LEFT JOIN equivalente_concorrente EC ON EC.id_concorrente = C.id_concorrente
                LEFT JOIN produto P ON P.id_produto = EC.id_produto
                WHERE C.id_concorrente = {id};
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
    return ({
        "id_concorrente": row[0][0],
        "id_equivalente_concorrente": lista_id,
        "modelo": lista_modelo,
        "codigo_concorrente": row[0][3],
        "descricao_concorrente": row[0][4],
        "empresa_concorrente": row[0][5],
        "observacao_concorrente": row[0][6]
    })