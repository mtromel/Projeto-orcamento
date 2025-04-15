# import sys
from pathlib import Path
from prettytable import PrettyTable

import utils

THIS_FOLDER = Path(__file__).parent.resolve()
con, cur = utils.conectar_bd(THIS_FOLDER / 'bd_orcamento.db')


def consulta_teste():
    cur.execute('SELECT r.id AS ID, r.descricao AS DESCRICAO, r.data AS DIA,'
                ' r.valor AS VALOR, per.periodo AS PERIODO FROM receitas AS r'
                ' INNER JOIN periodo AS per ON r.periodo_id=per.id WHERE'
                ' r.periodo_id = "3"')

    nomes_colunas = [description[0] for description in cur.description]
    linhas_despesas = cur.fetchall()

    return nomes_colunas, linhas_despesas


def imprimir_teste(nomes_colunas, linhas_despesas):
    tabela = PrettyTable()
    tabela.field_names = nomes_colunas
    for linha in linhas_despesas:
        tabela.add_row(linha)

    print(tabela)


name_col, line_table = consulta_teste()
imprimir_teste(name_col, line_table)
