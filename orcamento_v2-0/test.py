# import sys
from pathlib import Path
from prettytable import PrettyTable
# from datetime import datetime

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


# name_col, line_table = consulta_teste(cur, '*', 'periodo', 'periodo', '25')
# imprimir_teste(name_col, line_table)
# per = '3'
# per_completo = line_table[int(per) - 1][1]

# data_completa = ('8' + '/' + per_completo)
# data_convertida = datetime.strptime(data_completa, '%d/%b/%y')
# data_formatada = data_convertida.strftime('%d/%m/%Y')

# print(data_completa, '>>>', data_convertida, '>>>', data_formatada)

'''
menu de alteração de grupos de planejamento removido temporariamente
# Chama a função de alteração de grupos de planejamento
# cadastrados
os.system('cls')
utils.print_cabecalho(
    'LISTA DOS GRUPOS DE PLANEJAMENTO CADASTRADOS')

# Consulta os grupos de planejamento cadastrados e imprime
# na tela
consultas.consulta_padrao(cur, 'planejamento')

# Carrega em memória os grupos de planejamento cadastrados
# sem imprimir na tela
listagem = consultas.consulta_padrao_sem_imprimir(
    cur, 'planejamento')
grupo = input('Digite o id do grupo do planejamento que'
                ' deseja alterar: ')
if listagem:
    if grupo not in [str(linha[0]) for linha in listagem]:
        print('ID informado não encontrado.')
        input('Pressione ENTER para continuar...')
    else:
        os.system('cls')
        consultas.consulta_com_where(
            cur, 'planejamento', 'id', grupo)
        alterar.alterar_planejamento(cur, con, grupo)
else:
    print('Nenhum registro encontrado.')
    input('Pressione ENTER para continuar...')
'''
'''
menu de exclusão de grupos de planejamento removido temporariamente
# Chama a função de exclusão apropriada para grupos de
# planejamento cadastrados
os.system('cls')
utils.print_cabecalho('LISTA DE GRUPOS DE PLANEJAMENTO')

# Consulta os grupos de planejamento cadastrados e imprime
# na tela
linha, col = consultas.consulta_padrao(cur, 'planejamento')
utils.imprimir_tabelas(linha, col)

tipo = input('Deseja apagar um registro apenas? Digite'
                ' 1.\n'
                'Deseja apagar todos os registros da tabela?'
                ' Digite 2. \n'
                'SELECIONE A OPÇÃO DESEJADA: ')
if tipo == '1':
    deletar.apagar_registro(con, cur, 'planejamento')
elif tipo == '2':
    deletar.apagar_todos_registros(
        con, cur, 'planejamento')
else:
    input('Opção inválida, tente novamente. Pressione'
            ' ENTER para continuar')
'''


def input_com_placeholder(mensagem, placeholder):
    texto = (mensagem + ": " + placeholder + " \n Pressione ENTER para usar o"
             " atual. Ou digite um novo: ")
    entrada = input(texto)
    if entrada == "":
        return placeholder
    else:
        return entrada


# Exemplo de utilização
nome_bd = 'Marcos'
idade_bd = '45'
nome = input_com_placeholder("O valor atual desse campo é", nome_bd)
print(f"O nome é: {nome}")

idade = input_com_placeholder("Digite a sua idade", idade_bd)
print(f"A idade é: {idade}")
