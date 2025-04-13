import utils


# Função para consultar dados de uma tabela sem condições
def consulta_padrao(cur, tabela):
    consulta = 'SELECT * FROM {}'
    utils.imprimir_tabelas(cur, tabela, consulta, tabela)


def consulta_padrao_com_inner(cur, tabela):
    if tabela == 'despesas':
        consulta = ('SELECT d.id, d.desc_loja, d.desc_desp, d.data, d.valor,'
                    ' c.categoria, d.parcela_atual, d.parcelas_total, p.grupo,'
                    ' d.tipo, o.origem, per.periodo FROM despesas AS d INNER'
                    ' JOIN categorias AS c ON d.categoria_id=c.id INNER JOIN'
                    ' planejamento AS p ON d.grupo_id=p.id INNER JOIN origem'
                    ' AS o ON d.origem_id=o.id INNER JOIN periodo AS per ON'
                    ' d.periodo_id=per.id')
    elif tabela == 'desp_fixa':
        consulta = ('SELECT d.id, d.descricao, d.dia, c.categoria, d.valor,'
                    ' p.grupo, o.origem FROM desp_fixa AS d INNER'
                    ' JOIN categorias AS c ON d.categoria_id=c.id INNER JOIN'
                    ' planejamento AS p ON d.grupo_id=p.id INNER JOIN origem'
                    ' AS o ON d.origem_id=o.id')
    elif tabela == 'receitas':
        consulta = ('SELECT r.id, r.descricao, r.data, r.valor, per.periodo'
                    ' FROM receitas AS r INNER JOIN periodo AS per ON'
                    ' r.periodo_id=per.id')

    utils.imprimir_tabelas(cur, tabela, consulta, tabela)


def consulta_padrao_com_inner_where(cur, tabela, campo, valor):
    if tabela == 'despesas':
        consulta = (f'SELECT d.id, d.desc_loja, d.desc_desp, d.data, d.valor,'
                    f' c.categoria, d.parcela_atual, d.parcelas_total,'
                    f' p.grupo, d.tipo, o.origem, per.periodo FROM despesas AS'
                    f' d INNER JOIN categorias AS c ON d.categoria_id=c.id'
                    f' INNER JOIN planejamento AS p ON d.grupo_id=p.id INNER'
                    f' JOIN origem AS o ON d.origem_id=o.id INNER JOIN periodo'
                    f' AS per ON d.periodo_id=per.id WHERE'
                    f' {campo} = "{valor}"')
    elif tabela == 'desp_fixa':
        consulta = (f'SELECT d.id, d.descricao, d.dia, c.categoria, d.valor,'
                    f' p.grupo, o.origem FROM desp_fixa AS d INNER'
                    f' JOIN categorias AS c ON d.categoria_id=c.id INNER JOIN'
                    f' planejamento AS p ON d.grupo_id=p.id INNER JOIN origem'
                    f' AS o ON d.origem_id=o.id WHERE {campo} = "{valor}"')
    elif tabela == 'receitas':
        consulta = (f'SELECT r.id, r.descricao, r.data, r.valor, per.periodo'
                    f' FROM receitas AS r INNER JOIN periodo AS per ON'
                    f' r.periodo_id=per.id WHERE {campo} = "{valor}"')

    utils.imprimir_tabelas(cur, tabela, consulta, '')


# Função para consultar dados de uma tabela com condição WHERE
def consulta_com_where(cur, tabela, campo, valor):
    consulta = f'SELECT * FROM {tabela} WHERE {campo} = "{valor}"'
    utils.imprimir_tabelas(cur, tabela, consulta, '')


# Função para consultar dados de uma tabela com condição LIKE
def consulta_com_like(cur, coluna, tabela, campo, valor):
    consulta = f'SELECT {coluna} FROM {tabela} WHERE {campo} LIKE "%{valor}%"'
    utils.imprimir_tabelas(cur, tabela, consulta, '')


# Função para consultar dados de uma tabela sem condições e sem imprimir
def consulta_padrao_sem_imprimir(cur, tabela):
    consulta = f'SELECT * FROM {tabela}'
    cur.execute(consulta)
    return cur.fetchall()


# Função para consultar dados de uma tabela com condição WHERE e sem imprimir
def consulta_com_where_sem_imprimir(cur, coluna, tabela, campo, valor):
    consulta = f'SELECT {coluna} FROM {tabela} WHERE {campo} = "{valor}"'
    cur.execute(consulta)
    return cur.fetchall()


# Função para consultar dados de uma tabela com condição LIKE e sem imprimir
def consulta_com_like_sem_imprimir(cur, coluna, tabela, campo, valor):
    consulta = f'SELECT {coluna} FROM {tabela} WHERE {campo} LIKE "%{valor}%"'
    cur.execute(consulta)
    return cur.fetchall()
