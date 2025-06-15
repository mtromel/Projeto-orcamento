from prettytable import PrettyTable
import consultas
import utils


# Função para pagar um registro de uma tabela
def apagar_registro(con, cur, tabela, linha, col):
    print()
    id_reg = int(input('Insira o número do registro que deseja apagar: '))

    # Verifica se o registro existe
    encontrado = False
    for linhas in linha:
        if linhas[0] == id_reg:
            impr_tabela = PrettyTable()
            impr_tabela.field_names = col
            impr_tabela.add_row(linhas)
            print()
            print(impr_tabela)
            print()
            conf = input('Confirma a exclusão do registro acima? Digite "S"'
                         ' para Sim e "N" para não: ').upper()
            if conf == 'S':
                cur.execute(f'DELETE FROM {tabela} WHERE id = ?', (id_reg,))
                con.commit()
                print()
                print('Registro apagado com sucesso')
                encontrado = True
                break
            else:
                print()
                print('Operação cancelada')
                encontrado = True
                break
    if not encontrado:
        print()
        print(f'Registro com ID {id_reg} não encontrado na tabela {tabela}')

    input('Pressione ENTER para continuar...')


# Função para apagar TODOS os registros de uma tabela
def apagar_todos_registros(con, cur, tabela):
    confirm = input(f'Tem certeza que deseja apagar TODOS os registros de'
                    f' {tabela}? Digite S para confirmar: ').upper()
    if confirm == 'S':
        cur.execute(f'DELETE FROM {tabela}')
        con.commit()
        print()
        print('Todos os registros da tabela foram apagados com sucesso')
        input('Pressione ENTER para continuar...')
    else:
        print()
        print('Operação cancelada')
        input('Pressione ENTER para continuar...')


# Função para apagar todos os registros de um periodo específico de uma tabela
def apagar_todos_reg_com_where(con, cur, tabela, campo, valor):
    linhas, colunas = consultas.consulta_com_where(cur, tabela, campo, valor)
    utils.imprimir_tabelas(linhas, colunas)
    print()

    confirm = input(f'Tem certeza que deseja apagar todos os registros da'
                    f' tabela {tabela} para o período {valor} listados acima?'
                    f' Digite S para confirmar: ').upper()
    if confirm == 'S':
        cur.execute(f'DELETE FROM {tabela} WHERE {campo} = ?', (valor,))
        con.commit()
        print()
        print(f'Todos os registros da tabela {tabela} do período {valor} foram'
              ' apagados com sucesso')
        input('Pressione ENTER para continuar...')
    else:
        print()
        input('Operação cancelada. Pressione ENTER para continuar...')
