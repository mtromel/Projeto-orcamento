import sys
from pathlib import Path

import utils

THIS_FOLDER = Path(__file__).parent.resolve()

con, cur = utils.conectar_bd(THIS_FOLDER / 'bd_orcamento.db')

if con:
    print('Conexão com o bd ok!')
else:
    print('Erro na conexão com o bd!')


def imprimir_tabelas(cur, tabela, consulta, variavel):
    cur.execute('PRAGMA table_info({})'.format(tabela))
    colunas = [tupla[1] for tupla in cur.fetchall()]

    tam = 0
    num_colunas = (len(colunas) - 1)
    tam_colunas = []

    for coluna in colunas:
        # if coluna == 'id':
        #     tam_colunas.append(0)
        #     continue

        tam = tam + (len(coluna) + 3)
        tam_colunas.append(len(coluna))

    print('-' * (tam - 1))
    for coluna in colunas:
        # if coluna == 'id':
        #     continue
        print(coluna, end=' ' * ((tam_colunas[colunas.index(coluna)] + 3) -
                                 tam_colunas[colunas.index(coluna)]))
    print()
    print('-' * (tam - 1))

    listagem = cur.execute(consulta.format(variavel))

    for linha in listagem:
        for i in range(num_colunas + 1):
            print(linha[i], end=' ' * ((tam_colunas[i] + 4) - tam_colunas[i]))
        print()
        print('-' * (tam - 1))

    print(f'tam_colunas: {tam_colunas}, num_colunas: {num_colunas}')


print(*sys.path, sep='\n')
consulta = ('SELECT d.id, d.desc_loja, d.desc_desp, d.data, d.valor,'
            ' c.categoria, d.parcela_atual, d.parcelas_total,'
            ' p.grupo, d.tipo, o.origem, per.periodo FROM despesas AS'
            ' d INNER JOIN categorias AS c ON d.categoria_id=c.id'
            ' INNER JOIN planejamento AS p ON d.grupo_id=p.id INNER'
            ' JOIN origem AS o ON d.origem_id=o.id INNER JOIN periodo'
            ' AS per ON d.periodo_id=per.id WHERE'
            ' d.periodo_id = "3"')

listagem = cur.execute(consulta)

resultado = listagem.fetchall()

print(*resultado, sep='\n')

for linha in resultado:
    for coluna in linha:
        print(coluna, end='   ')
    print()

print('função imprimir tabelas:')
imprimir_tabelas(cur, 'despesas', consulta, '')
