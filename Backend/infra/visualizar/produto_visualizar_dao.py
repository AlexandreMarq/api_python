# Imports
from mysql.connector import connect
from BD.banco import connection


def consultar(id):
    cursor = connection.cursor()
    sql = f"""select P.id_produto
        , P.descricao_completa
        , P.descricao_reduzida
        , P.link_codigo_pedido
        , P.link_dimensoes
        , P.link_esquema_ligacao
        , P.link_exemplo_ligacao
        , P.link_site
        , P.link_tabela_alarmes
        , P.link_tabela_parametros
        , P.modelo
        , P.status
        , Alimentacao.alimentacao
        , Aplicacao.aplicacao
        , AppNavegacao.aplicacao_navegacao
        , Categoria.categoria
        , CategoriaVenda.categoria_venda
        , Certificado.certificado
        , Foto.link_foto
        , Funcao.funcao
        , M.nome_manual
        , Montagem.montagem
    
    from produto P
    INNER JOIN alimentacao Alimentacao on Alimentacao.id_alimentacao = P.id_alimentacao
    INNER JOIN aplicacao Aplicacao on Aplicacao.id_aplicacao = P.id_aplicacao
    INNER JOIN aplicacao_navegacao AppNavegacao on AppNavegacao.id_aplicacao_navegacao = P.id_aplicacao_navegacao
    INNER JOIN categoria Categoria on Categoria.id_categoria = P.id_categoria
    INNER JOIN categoria_venda CategoriaVenda on CategoriaVenda.id_categoria = P.id_categoria_venda
    INNER JOIN certificado Certificado on Certificado.id_certificado = P.id_certificado
    INNER JOIN foto Foto on Foto.id_foto = P.id_foto
    INNER JOIN funcao Funcao on Funcao.id_funcao = P.id_funcao
    INNER JOIN manual M on M.id_manual = P.id_manual
    INNER JOIN montagem Montagem on Montagem.id_montagem = P.id_montagem
    WHERE P.id_produto = {id}
    """
    cursor.execute(sql)
    row = cursor.fetchone()
    if row is None:
        return None
    
    connection.commit()
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
             "alimentacao": row[12],
             "aplicacao": row[13],
             "aplicacao_navegacao": row[14],
             "categoria": row[15],
             "categoria_venda": row[16],
             "certificado": row[17],
             "foto": row[18],
             "funcao": row[19],
             "nome_manual": row[20],
             "montagem": row[21]})