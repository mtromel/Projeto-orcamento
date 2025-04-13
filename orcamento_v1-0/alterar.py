from datetime import datetime
import locale


locale.setlocale(locale.LC_ALL, 'pt_BR.UTF-8')
cabecalho_padrao = 'ALTERAÇÃO DE LANÇAMENTO DE '


# Função para alterar um registro da tabela despesas
def alterar_despesa(con, cur, per, id_desp):
    desc_lj = input('Insira o nome da despesa: ')
    desc_desp = input('Insira uma descrição para a despesa: ')
    while True:
        data = input('Insira a data da despesa no formato DD/MM/AAAA: ')

        try:
            data_convertida = datetime.strptime(data, '%d/%m/%Y')
            data_formatada = data_convertida.strftime('%d/%m/%Y')
            break
        except ValueError:
            print()
            print('Data inválida. Digite a data no formato DD/MM/AAAA')

    valor = input('Insira o valor da despesa: ')
    categ = input('Informe o id da categoria: ')
    num_parc = input(
        'Informe o número de parcelas (zero para despesa única): ')
    grp_plan = input('Informe o id do grupo de planejamento: ')
    tipo = input('Informe se a despesa é fixa ou variável: ').upper()
    org_desp = input('Informe o id da origem: ')

    if num_parc == '0':
        num_parc_atual = num_parc
    else:
        num_parc_atual = '1'

    cur.execute("UPDATE despesas SET desc_loja = ?, desc_desp = ?, data = ?,"
                " valor = ?, tipo = ?, parcelas_total = ?, categoria_id = ?,"
                " grupo_id = ?, origem_id = ?, periodo_id = ?, parcela_atual"
                " = ? WHERE id = ?", (desc_lj, desc_desp, data_formatada,
                                      valor, tipo, num_parc, categ, grp_plan,
                                      org_desp, per, num_parc_atual, id_desp))
    print()
    print('Despesa alterada com sucesso')
    con.commit()

    if num_parc != '0':
        print()
        print('------------------------------------------------')
        print()
        confirm = input('Deseja cadastrar as demais parcelas nos próximos'
                        ' períodos? (Caso a série de parcelas já tenha sido'
                        ' cadastrada você precisa alterar uma de cada vez, não'
                        ' use esse recurso com risco de duplicação de'
                        ' registros) Digite S para Sim e N para Não: ').upper()

        if confirm == 'S':
            prx_per = int(per)
            for i in range(2, int(num_parc) + 1):
                prx_per += 1
                cur.execute("INSERT INTO despesas (desc_loja,"
                            " desc_desp, data, valor, tipo,"
                            " parcelas_total, categoria_id, grupo_id,"
                            " origem_id, periodo_id, parcela_atual)"
                            " VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?,"
                            " ?)", (desc_lj, desc_desp, data, valor,
                                    tipo, num_parc, categ, grp_plan,
                                    org_desp, prx_per, i))
            con.commit()
            print()
            print('Série de parcelas cadastrada com sucesso')

    input('Pressione ENTER para continuar...')


# Função para alterar um registro da tabela categorias
def alterar_categoria(cur, con, id_cat):
    nome = input('Insira o novo nome da categoria: ')
    cur.execute("UPDATE categorias SET categoria = ? WHERE id = ?", (
        nome, id_cat))
    print()
    print('Categoria alterada com sucesso')
    con.commit()
    input('Pressione ENTER para continuar...')


# Função para alterar um registro da tabela planejamento
def alterar_planejamento(cur, con, id_gr_plan):
    nome = input('Insira o novo nome do grupo de planejamento: ')
    cur.execute("UPDATE planejamento SET grupo = ? WHERE id = ?", (
        nome, id_gr_plan))
    print()
    print('Grupo de planejamento alterado com sucesso')
    con.commit()
    input('Pressione ENTER para continuar...')


# Função para alterar um registro da tabela desp_fixa
def alterar_desp_fixa(cur, con, id_desp_fixa):
    desc = input('Insira a descrição da despesa: ')
    dia = int(input('Insira o dia fixo de vencimento: '))
    categoria = int(input('Insira o número da categoria: '))
    valor = float(input('Insira o valor fixo da despesa: '))
    grupo = int(input('Insira o número do grupo de planejamento: '))
    origem = int(input('Insira o número da origem: '))

    cur.execute('UPDATE desp_fixa SET descricao = ?, dia = ?, valor = ?,'
                ' categoria_id = ?, grupo_id = ?, origem_id = ? WHERE id = ?',
                (desc, dia, valor, categoria, grupo, origem, id_desp_fixa))
    con.commit()
    print('Despesa fixa alterada com sucesso')
    input('Pressione ENTER para continuar...')


# Função para alterar um registro da tabela origem
def alterar_origem(cur, con, id_org):
    nome = input('Insira o novo nome da origem: ')
    cur.execute("UPDATE origem SET origem = ? WHERE id = ?", (
        nome, id_org))
    print()
    print('Origem alterada com sucesso')
    con.commit()
    input('Pressione ENTER para continuar...')


# Função para alterar um registro da tabela receitas
def alterar_receitas(con, cur, per, id_rece):
    desc = input('Insira a descrição da receita: ')
    data = int(input('Insira o dia da receita: '))
    valor = float(input('Insira o valor da receita: '))

    cur.execute("UPDATE receitas SET descricao = ?, data = ?, valor = ?,"
                " periodo_id = ? WHERE id = ?", (desc, data, valor, per,
                                                 id_rece))
    print()
    print('Despesa alterada com sucesso')
    con.commit()
    input('Pressione ENTER para continuar...')


# Função para alterar um registro da tabela rec_templates
def alterar_rec_templates(con, cur, id_tpl):
    desc = input('Insira a descrição da receita: ')
    valor = float(input('Insira o valor da receita: '))
    data = int(input('Insira o dia da receita: '))

    cur.execute("UPDATE rec_templates SET descricao = ?, data = ?, valor = ?"
                " WHERE id = ?", (desc, data, valor, id_tpl))
    print()
    print('Template de receita alterada com sucesso')
    con.commit()
    input('Pressione ENTER para continuar...')
