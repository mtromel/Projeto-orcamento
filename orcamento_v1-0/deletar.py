# Função para pagar um registro de uma tabela
def apagar_registro(con, cur, tabela):
    id_reg = int(input('Insira o número do registro que deseja apagar: '))
    cur.execute(f'DELETE FROM {tabela} WHERE id = ?', (id_reg,))
    con.commit()
    print()
    print('Registro apagado com sucesso')
    input('Pressione ENTER para continuar...')


# Função para apagar TODOS os registros de uma tabela
def apagar_todos_registros(con, cur, tabela):
    confirm = input(f'Tem certeza que deseja apagar todos os registros de'
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
    confirm = input(f'Tem certeza que deseja apagar todos os registros da'
                    f' tabela {tabela} para o período {valor}? Digite S para'
                    f' confirmar: ').upper()
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
