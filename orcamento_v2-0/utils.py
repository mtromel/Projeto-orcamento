import sqlite3
from prettytable import PrettyTable


# Função para criar a conexão e o cursor do banco de dados e retorná-los
def conectar_bd(db_path):
    try:
        con = sqlite3.connect(db_path)
        cur = con.cursor()
        return con, cur
    except sqlite3.Error as e:
        print(f'Erro ao conectar ao banco de dados: {e}')
        return None, None


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


# Função para imprimir as tabelas do banco de dados
def imprimir_tabelas(linhas_despesas, nomes_colunas):
    tabela = PrettyTable()
    tabela.field_names = nomes_colunas
    for linha in linhas_despesas:
        tabela.add_row(linha)

    print(tabela)


# Função para usar placeholder nas alterações de dados
def input_com_placeholder(mensagem: str, placeholder: str):
    texto = (mensagem + ": " + placeholder + " \n Pressione ENTER para usar o"
             " valor padrão. Ou digite um novo valor: ")
    entrada = input(texto)
    if entrada == "":
        return placeholder
    else:
        return entrada
