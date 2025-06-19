"""
Autor: Marcos Cristiano Trömel
Data: 09/04/2025
Descrição: Funções para consultas ao banco de dados.
"""


# Função para consultar dados de uma tabela sem condições
def consulta_padrao(cur, tabela):
    cur.execute(f'SELECT * FROM {tabela}')

    nomes_colunas = [description[0] for description in cur.description]
    linhas_tabela = cur.fetchall()

    return linhas_tabela, nomes_colunas


# Função para consultar dados de uma tabela com INNER JOIN e sem condições
# pode ser usad para consultar despesas, despesas fixas e receitas
def consulta_padrao_com_inner(cur, tabela):
    if tabela == 'despesas':
        cur.execute('SELECT d.id AS ID, d.desc_loja AS DESCRICAO, d.data AS'
                    ' DATA, d.valor AS VALOR, c.categoria AS CATEGORIA,'
                    ' d.parcela_atual AS "PARC ATUAL", d.parcelas_total AS'
                    ' "TOTAL PARC", p.grupo AS "GR PLAN", d.tipo AS TIPO,'
                    ' o.origem AS ORIGEM, per.periodo AS PERIODO FROM'
                    ' despesas AS d INNER JOIN categorias AS c ON'
                    ' d.categoria_id=c.id INNER JOIN planejamento AS p ON'
                    ' d.grupo_id=p.id INNER JOIN origem AS o ON'
                    ' d.origem_id=o.id INNER JOIN periodo AS per ON'
                    ' d.periodo_id=per.id')
    elif tabela == 'desp_fixa':
        cur.execute('SELECT d.id AS ID, d.descricao AS DESCRICAO, d.dia AS'
                    ' DIA, c.categoria AS CATEGORIA, d.valor AS VALOR,'
                    ' p.grupo AS "GR PLAN", o.origem AS ORIGEM FROM'
                    ' desp_fixa AS d INNER JOIN categorias AS c ON'
                    ' d.categoria_id=c.id INNER JOIN planejamento AS p ON'
                    ' d.grupo_id=p.id INNER JOIN origem AS o ON'
                    ' d.origem_id=o.id')
    elif tabela == 'receitas':
        cur.execute('SELECT r.id AS ID, r.descricao AS DESCRICAO, r.data AS'
                    ' DATA, r.valor AS VALOR, per.periodo AS PERIODO FROM'
                    ' receitas AS r INNER JOIN periodo AS per ON'
                    ' r.periodo_id=per.id')

    nomes_colunas = [description[0] for description in cur.description]
    linhas_tabela = cur.fetchall()

    return linhas_tabela, nomes_colunas


# Função para consultar dados de uma tabela com INNER JOIN e condição WHERE
# pode ser usada para consultar despesas, despesas fixas e receitas
def consulta_padrao_com_inner_where(cur, tabela, campo, valor):
    if tabela == 'despesas':
        cur.execute(f'SELECT d.id AS ID, d.desc_loja AS DESCRICAO, d.data'
                    f' AS DATA, d.valor AS VALOR, c.categoria AS CATEGORIA,'
                    f' d.parcela_atual AS "PARC ATUAL", d.parcelas_total AS'
                    f' "TOTAL PARC", p.grupo AS "GR PLAN", d.tipo AS TIPO,'
                    f' o.origem AS ORIGEM, per.periodo AS PERIODO FROM'
                    f' despesas AS d INNER JOIN categorias AS c ON'
                    f' d.categoria_id=c.id INNER JOIN planejamento AS p ON'
                    f' d.grupo_id=p.id INNER JOIN origem AS o ON'
                    f' d.origem_id=o.id INNER JOIN periodo AS per ON'
                    f' d.periodo_id=per.id WHERE {campo} = "{valor}"')
    elif tabela == 'desp_fixa':
        cur.execute(f'SELECT d.id AS ID, d.descricao AS DESCRICAO, d.dia AS'
                    f' DIA, c.categoria AS CATEGORIA, d.valor AS VALOR,'
                    f' p.grupo AS "GR PLAN", o.origem AS ORIGEM FROM'
                    f' desp_fixa AS d INNER JOIN categorias AS c ON'
                    f' d.categoria_id=c.id INNER JOIN planejamento AS p ON'
                    f' d.grupo_id=p.id INNER JOIN origem AS o ON'
                    f' d.origem_id=o.id WHERE {campo} = "{valor}"')
    elif tabela == 'receitas':
        cur.execute(f'SELECT r.id AS ID, r.descricao AS DESCRICAO, r.data '
                    f'AS DIA, r.valor AS VALOR, per.periodo AS PERIODO'
                    f' FROM receitas AS r INNER JOIN periodo AS per ON'
                    f' r.periodo_id=per.id WHERE {campo} = "{valor}"')

    nomes_colunas = [description[0] for description in cur.description]
    linhas_tabela = cur.fetchall()

    return linhas_tabela, nomes_colunas


# Função para consultar dados de uma tabela com condição WHERE
def consulta_com_where(cur, tabela, campo, valor):
    cur.execute(f'SELECT * FROM {tabela} WHERE {campo} = "{valor}"')

    nomes_colunas = [description[0] for description in cur.description]
    linhas_tabela = cur.fetchall()

    return linhas_tabela, nomes_colunas


# Função para consultar dados de uma tabela com condição LIKE
def consulta_com_like(cur, coluna, tabela, campo, valor):
    cur.execute(f'SELECT {coluna} FROM {tabela} WHERE {campo} LIKE'
                f' "%{valor}%"')

    nomes_colunas = [description[0] for description in cur.description]
    linhas_tabela = cur.fetchall()

    return linhas_tabela, nomes_colunas
