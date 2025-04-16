import sqlite3
from prettytable import PrettyTable


# Função para criar a conexão e o cursor do banco de dados e retorná-los
def conectar_bd(banco):
    con = sqlite3.connect(banco)
    cur = con.cursor()
    return con, cur


# Função para imprimir o cabeçalho de uma tela
def print_cabecalho(cabecalho):
    tam = len(cabecalho)
    print(cabecalho)
    print('-' * tam)
    print()


# Função para controlar se o usuário deseja continuar ou não com a rotina
def reiniciar_loop(rotina):
    print()
    continua = input(f'Deseja lançar mais {rotina}? Digite "S" para Sim ou'
                     ' "N" para não: ').upper()
    if continua == 'S':
        return 'continue'
    else:
        print()
        return 'break'

# def imprimir_tabelas(cur, tabela, consulta, variavel):
#     cur.execute('PRAGMA table_info({})'.format(tabela))
#     colunas = [tupla[1] for tupla in cur.fetchall()]

#     tam = 0
#     num_colunas = (len(colunas) - 1)
#     tam_colunas = []

#     for coluna in colunas:
#         # if coluna == 'id':
#         #     tam_colunas.append(0)
#         #     continue

#         tam = tam + (len(coluna) + 3)
#         tam_colunas.append(len(coluna))

#     print('-' * (tam - 1))
#     for coluna in colunas:
#         # if coluna == 'id':
#         #     continue
#         print(coluna, end=' ' * ((tam_colunas[colunas.index(coluna)] + 3) -
#                                  tam_colunas[colunas.index(coluna)]))
#     print()
#     print('-' * (tam - 1))

#     listagem = cur.execute(consulta.format(variavel))

#     for linha in listagem:
#         for i in range(num_colunas + 1):
#             print(linha[i], end=' ' * ((tam_colunas[i] + 4)-tam_colunas[i]))
#         print()
#         print('-' * (tam - 1))


# Função para imprimir as tabelas do banco de dados
def imprimir_tabelas(linhas_despesas, nomes_colunas):
    tabela = PrettyTable()
    tabela.field_names = nomes_colunas
    for linha in linhas_despesas:
        tabela.add_row(linha)

    print(tabela)


# def imprimir_tabelas(cur, tabela, consulta, variavel):
#     cur.execute('PRAGMA table_info({})'.format(tabela))
#     colunas = [tupla[1] for tupla in cur.fetchall()]

#     tam = 0
#     num_colunas = len(colunas)
#     tam_colunas = []
#     for coluna in colunas:
#         tam = tam + (len(coluna) + 3)
#         tam_colunas.append(len(coluna))

#     print('-' * (tam - 1))
#     for coluna in colunas:
#         print(coluna, end=' ' * ((tam_colunas[colunas.index(coluna)] + 3) -
#                                  tam_colunas[colunas.index(coluna)]))
#     print()
#     print('-' * (tam - 1))

#     listagem = cur.execute(consulta.format(variavel))

#     for linha in listagem:
#         for i in range(num_colunas):
#             if i == 0:
#                 if linha[i] < 10:
#                     print(linha[i], end=' ' * ((tam_colunas[i] + 4) -
#                                                tam_colunas[i]))
#                 elif linha[i] >= 10 and linha[i] < 100:
#                     print(linha[i], end=' ' * ((tam_colunas[i] + 3) -
#                                                tam_colunas[i]))
#                 else:
#                     print(linha[i], end=' ' * ((tam_colunas[i] + 2) -
#                                                tam_colunas[i]))
#             else:
#                 print(linha[i], end=' ; ')
#         print()
#         print('-' * (tam - 1))
