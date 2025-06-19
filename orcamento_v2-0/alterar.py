from datetime import datetime
import locale
import utils


locale.setlocale(locale.LC_ALL, 'pt_BR.UTF-8')
cabecalho_padrao = 'ALTERAÇÃO DE LANÇAMENTO DE '


# Função para alterar um registro da tabela despesas
def alterar_despesa(con, cur, per, id_desp, cons: list):
    desc_lj_bd = cons[0][1]
    desc_desp_bd = cons[0][2]
    data_bd = cons[0][3]
    data_bd_str = str(data_bd)
    valor_bd = cons[0][4]
    valor_bd_str = str(valor_bd)
    categ_bd = cons[0][5]
    categ_bd_str = str(categ_bd)
    num_parc_bd = cons[0][7]
    num_parc_bd_str = str(num_parc_bd)
    grp_plan_bd = cons[0][8]
    grp_plan_bd_str = str(grp_plan_bd)
    tipo_bd = cons[0][9]
    org_desp_bd = cons[0][10]
    org_desp_bd_str = str(org_desp_bd)

    desc_lj = utils.input_com_placeholder(
        'O atual nome da despesa é', desc_lj_bd)
    if desc_desp_bd is None:
        desc_desp_bd = ''
    desc_desp = utils.input_com_placeholder(
        'A atual descrição da despesa é', desc_desp_bd)
    while True:
        data = utils.input_com_placeholder(
            'A atual data da despesa é', data_bd_str)

        try:
            data_convertida = datetime.strptime(data, '%d/%m/%Y')
            data_formatada = data_convertida.strftime('%d/%m/%Y')
            break
        except ValueError:
            print()
            print('Data inválida. Digite a data no formato DD/MM/AAAA')
    while True:
        valor_in = utils.input_com_placeholder(
            'O atual valor da despesa é', valor_bd_str).replace(',', '.')

        try:
            if valor_in:
                valor = float(valor_in)
                break
            else:
                print('Valor inválido. Insira um valor válido')
                continue
        except ValueError:
            print('Valor inválido. Insira um valor válido')
            continue

    categ = utils.input_com_placeholder(
        'A atual categoria é', categ_bd_str)
    num_parc = utils.input_com_placeholder(
        'O número atual de parcelas é', num_parc_bd_str)
    grp_plan = utils.input_com_placeholder(
        'O atual grupo de planejamento é', grp_plan_bd_str)

    while True:
        tipo_in = utils.input_com_placeholder(
            'O tipo de despesa atual é', tipo_bd)

        if tipo_in == tipo_bd:
            tipo = tipo_bd
            break
        elif tipo_in == 'F':
            tipo = 'FIXA'
            break
        elif tipo_in == 'V':
            tipo = 'VARIAVEL'
            break
        else:
            input('Opção inválida. Tecle ENTER para tentar novamente')
            continue

    org_desp = utils.input_com_placeholder(
        'O atual id da origem é', org_desp_bd_str)

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
    con.commit()
    print('Despesa alterada com sucesso')

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
def alterar_categoria(cur, con, id_cat, nome_bd, cons):
    duplicado = False
    nome = utils.input_com_placeholder(
        'O atual nome da categoria é', nome_bd)

    if nome != nome_bd:
        for linha in cons:
            categoria = linha[1]

            if nome == categoria:
                print()
                print('Nome de categoria já existe')
                print()
                input('Pressione ENTER para continuar...')
                duplicado = True
                break

    if not duplicado:
        cur.execute("UPDATE categorias SET categoria = ? WHERE id = ?", (
            nome, id_cat))

        print()
        con.commit()
        print('Categoria alterada com sucesso')

        input('Pressione ENTER para continuar...')


# Função para alterar um registro da tabela desp_fixa
def alterar_desp_fixa(cur, con, id_desp_fixa, cons: list):

    desc_bd = cons[0][1]
    dia_bd = cons[0][2]
    dia_bd_str = str(dia_bd)
    cat_bd = cons[0][3]
    cat_bd_str = str(cat_bd)
    valor_bd = cons[0][4]
    valor_bd_str = str(valor_bd)
    grp_bd = cons[0][5]
    grp_bd_str = str(grp_bd)
    origem_bd = cons[0][6]
    origem_bd_str = str(origem_bd)

    desc = utils.input_com_placeholder(
        'A atual descrição da despesa é', desc_bd)
    dia = utils.input_com_placeholder(
        'O atual dia fixo de vencimento é', dia_bd_str)
    categoria = utils.input_com_placeholder(
        'O atual número da categoria é', cat_bd_str)

    while True:
        valor_in = utils.input_com_placeholder(
            'O atual valor da despesa é', valor_bd_str).replace(',', '.')

        try:
            if valor_in:
                valor = float(valor_in)
                break
            else:
                print('Valor inválido. Insira um valor válido')
                continue
        except ValueError:
            print('Valor inválido. Insira um valor válido')
            continue

    grupo = utils.input_com_placeholder(
        'O atual grupo de planejamento é', grp_bd_str)
    origem = utils.input_com_placeholder(
        'A atual origem é', origem_bd_str)

    cur.execute('UPDATE desp_fixa SET descricao = ?, dia = ?, valor = ?,'
                ' categoria_id = ?, grupo_id = ?, origem_id = ? WHERE id = ?',
                (desc, dia, valor, categoria, grupo, origem, id_desp_fixa))
    con.commit()
    print('Despesa fixa alterada com sucesso')
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


# Função para alterar um registro da tabela origem
def alterar_origem(cur, con, id_org, nome_bd, cons):
    duplicado = False
    nome = utils.input_com_placeholder(
        'O atual nome da origem é', nome_bd)

    if nome != nome_bd:
        for linha in cons:
            origem = linha[1]

            if nome == origem:
                print()
                print('Nome de origem já existe')
                print()
                input('Pressione ENTER para continuar...')
                duplicado = True
                break

    if not duplicado:
        cur.execute("UPDATE origem SET origem = ? WHERE id = ?", (
            nome, id_org))
        print()
        con.commit()
        print('Origem alterada com sucesso')
        input('Pressione ENTER para continuar...')


# Função para alterar um registro da tabela receitas
def alterar_receitas(con, cur, per, id_rece, cons: list):
    desc_bd = cons[0][1]
    data_bd = cons[0][2]
    data_bd_str = str(data_bd)
    valor_bd = cons[0][3]
    valor_bd_str = str(valor_bd)

    desc = utils.input_com_placeholder(
        'A atual descrição da receita é', desc_bd)
    data = utils.input_com_placeholder(
        'O dia atual da receita é', data_bd_str)

    while True:
        valor_in = utils.input_com_placeholder(
            'O atual valor da receita é', valor_bd_str).replace(',', '.')

        try:
            if valor_in:
                valor = float(valor_in)
                break
            else:
                print('Valor inválido. Insira um valor válido')
                continue
        except ValueError:
            print('Valor inválido. Insira um valor válido')
            continue

    cur.execute("UPDATE receitas SET descricao = ?, data = ?, valor = ?,"
                " periodo_id = ? WHERE id = ?", (desc, data, valor, per,
                                                 id_rece))
    print()
    con.commit()
    print('Despesa alterada com sucesso')
    input('Pressione ENTER para continuar...')


# Função para alterar um registro da tabela rec_templates
def alterar_rec_templates(
        con, cur, id_tpl, cons: list):
    desc_bd = cons[0][1]
    valor_bd = cons[0][2]
    valor_bd_str = str(valor_bd)
    data_bd = cons[0][3]
    data_bd_str = str(data_bd)

    desc = utils.input_com_placeholder(
        'A atual descrição da receita é', desc_bd)

    while True:
        valor_in = utils.input_com_placeholder(
            'O atual valor da receita é', valor_bd_str).replace(',', '.')

        try:
            if valor_in:
                valor = float(valor_in)
                break
            else:
                print('Valor inválido. Insira um valor válido')
                continue
        except ValueError:
            print('Valor inválido. Insira um valor válido')
            continue

    data = utils.input_com_placeholder('O dia atual da receita é', data_bd_str)
    cur.execute("UPDATE rec_templates SET descricao = ?, data = ?, valor = ?"
                " WHERE id = ?", (desc, data, valor, id_tpl))
    print()
    con.commit()
    print('Template de receita alterada com sucesso')
    input('Pressione ENTER para continuar...')
