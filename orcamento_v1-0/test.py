# import sys
from pathlib import Path
from prettytable import PrettyTable
from datetime import datetime

import utils

THIS_FOLDER = Path(__file__).parent.resolve()
con, cur = utils.conectar_bd(THIS_FOLDER / 'bd_orcamento.db')


def consulta_teste(cur, coluna, tabela, campo, valor):
    cur.execute(f'SELECT {coluna} FROM {tabela} WHERE {campo} LIKE'
                f' "%{valor}%"')
    # cur.execute(f'SELECT * FROM periodo WHERE periodo LIKE "%25%"')

    nomes_colunas = [description[0] for description in cur.description]
    linhas_despesas = cur.fetchall()

    return nomes_colunas, linhas_despesas


def imprimir_teste(nomes_colunas, linhas_despesas):
    tabela = PrettyTable()
    tabela.field_names = nomes_colunas
    for linha in linhas_despesas:
        tabela.add_row(linha)

    print(tabela)


name_col, line_table = consulta_teste(cur, '*', 'periodo', 'periodo', '25')
imprimir_teste(name_col, line_table)
per = '3'
per_completo = line_table[int(per) - 1][1]

data_completa = ('8' + '/' + per_completo)
data_convertida = datetime.strptime(data_completa, '%d/%b/%y')
data_formatada = data_convertida.strftime('%d/%m/%Y')

print(data_completa, '>>>', data_convertida, '>>>', data_formatada)
