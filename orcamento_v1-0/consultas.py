import utils


# Função para consultar dados de uma tabela sem condições
def consulta_padrao(cur, tabela):
    consulta = 'SELECT * FROM {}'
    utils.imprimir_tabelas(cur, tabela, consulta, tabela)


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
