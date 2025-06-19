import utils
import locale
import os
from datetime import datetime
import consultas


locale.setlocale(locale.LC_ALL, 'pt_BR.UTF-8')
cabecalho_padrao = 'CADASTRO DE '


# Função para cadastrar as origens de despesas
def cadastro_origens(con, cur):
    while True:
        os.system('cls')
        cabecalho = cabecalho_padrao + 'ORIGENS'
        utils.print_cabecalho(cabecalho)
        print('Origens cadastradas:')
        linha, col = consultas.consulta_padrao(cur, 'origem')
        utils.imprimir_tabelas(linha, col)
        origem = input('Insira a nova origem: ')

        consulta, _ = consultas.consulta_com_like(cur, 'origem', 'origem',
                                                  'origem', origem)
        if consulta:
            print('Origem já existe')
        else:
            cur.execute('INSERT INTO origem (origem) VALUES (?)', (origem,))
            con.commit()
            print('Origem inserida com sucesso')

        continua = utils.reiniciar_loop('origens')
        if continua == 'continue':
            continue
        else:
            print()
            break


# Função para cadastrar os grupos de planejamento
def cadastro_planejamento(con, cur):
    while True:
        os.system('cls')
        cabecalho = cabecalho_padrao + 'GRUPOS DE PLANEJAMENTO'
        utils.print_cabecalho(cabecalho)
        print('Grupos de planejamento cadastrados:')
        linhas, col = consultas.consulta_padrao(cur, 'planejamento')
        utils.imprimir_tabelas(linhas, col)
        grupo = input('Digite o grupo do planejamento que deseja incluir: ')

        consulta, _ = consultas.consulta_com_like(cur, 'grupo', 'planejamento',
                                                  'grupo', grupo)

        if consulta:
            print('Planejamento já cadastrado')
        else:
            cur.execute("INSERT INTO planejamento (grupo) VALUES (?)",
                        (grupo,))
            con.commit()
            print('Planejamento incluido com sucesso')

        continua = utils.reiniciar_loop('grupos de planejamento')
        if continua == 'continue':
            continue
        else:
            print()
            break


# Função para cadastrar as categorias de despesas
def cadastra_categorias(con, cur):
    while True:
        os.system('cls')
        cabecalho = cabecalho_padrao + 'CATEGORIAS'
        utils.print_cabecalho(cabecalho)
        print('Categorias cadastradas:')
        linhas, col = consultas.consulta_padrao(cur, 'categorias')
        utils.imprimir_tabelas(linhas, col)
        categoria = input('Insira a nova categoria: ')
        consulta, _ = consultas.consulta_com_like(cur, 'categoria',
                                                  'categorias', 'categoria',
                                                  categoria)
        if consulta:
            print('Categoria já exite')
        else:
            cur.execute('INSERT INTO categorias (categoria) VALUES (?)',
                        (categoria,))
            con.commit()
            print('Categoria inserida com sucesso')

        continua = utils.reiniciar_loop('categorias')
        if continua == 'continue':
            continue
        else:
            print()
            break


# Função para cadastrar os períodos de lançamentos
def cadastro_periodo(con, cur):
    while True:
        os.system('cls')
        cabecalho = cabecalho_padrao + 'PERÍODOS'
        utils.print_cabecalho(cabecalho)
        year = int(input('Digite o ano do periodo que deseja incluir no'
                         ' formato ##:'))

        if year <= 99:
            year_str = str(year)
            retorno, _ = consultas.consulta_com_like(cur, 'periodo', 'periodo',
                                                     'periodo', year_str)

            if retorno:
                print('Periodo já cadastrado')
            else:
                meses = ('jan/', 'fev/', 'mar/', 'abr/', 'mai/', 'jun/',
                         'jul/', 'ago/', 'set/', 'out/', 'nov/', 'dez/')
                for mes in meses:
                    periodo = mes + year_str
                    cur.execute("INSERT INTO periodo (periodo) VALUES (?)",
                                (periodo,))

                con.commit()

                print('Periodo incluido com sucesso')

        else:
            print('Ano inválido. Insira um ano válido no formato ##')

        print()
        print('------------------------------------------------')
        print('Períodos cadastrados:')
        periodo, col = consultas.consulta_padrao(cur, 'periodo')
        utils.imprimir_tabelas(periodo, col)

        continua = utils.reiniciar_loop('períodos')
        if continua == 'continue':
            continue
        else:
            print()
            break


# Função para cadastrar os templates de receitas que são usadas para lançar as
# receitas mensais
def cadastro_templates_receitas(con, cur):
    while True:
        os.system('cls')
        cabecalho = cabecalho_padrao + 'TEMPLATES DE RECEITAS'
        utils.print_cabecalho(cabecalho)
        print('Templates de receitas já cadastrados:')
        linha, col = consultas.consulta_padrao(cur, 'rec_templates')
        utils.imprimir_tabelas(linha, col)
        confirm = input('Deseja cadastrar um novo template de receita? Digite'
                        ' S para Sim e N para Não: ').upper()

        if confirm == 'S':
            desc = input('Insira a descrição da receita: ')
            dia = int(input('Insira o dia fixo de recebimento: '))
            valor = float(input('Insira o valor fixo da receita: '))

            cur.execute('INSERT INTO rec_templates (descricao, data, valor)'
                        ' VALUES (?, ?, ?)', (desc, dia, valor))

            con.commit()
            print('Template de receita cadastrada com sucesso')

            continua = utils.reiniciar_loop('templates de receitas')
            if continua == 'continue':
                continue
            else:
                print()
                break
        else:
            print()
            break


# Função para cadastrar as despesas fixas
def cadastro_despesas_fixas(con, cur):
    while True:
        os.system('cls')
        cabecalho = cabecalho_padrao + 'DESPESAS FIXAS'
        utils.print_cabecalho(cabecalho)
        print('Despesas fixas já cadastradas:')
        linhas, col = consultas.consulta_padrao(cur, 'desp_fixa')
        utils.imprimir_tabelas(linhas, col)
        confirm = input('Deseja cadastrar uma nova despesa fixa? Digite S para'
                        ' Sim e N para Não: ').upper()

        if confirm == 'S':
            desc = input('Insira a descrição da despesa: ')
            dia = int(input('Insira o dia fixo de vencimento: '))
            valor = float(input('Insira o valor fixo da despesa: '))
            print()
            print('--------------------------------------------')
            print('Categorias cadastradas:')
            linhas, col = consultas.consulta_padrao(cur, 'categorias')
            utils.imprimir_tabelas(linhas, col)
            categoria = int(input('Insira o número da categoria: '))
            print()
            print('--------------------------------------------')
            print('Grupos de planejamento cadastrados: ')
            linhas, col = consultas.consulta_padrao(cur, 'planejamento')
            utils.imprimir_tabelas(linhas, col)
            grupo = int(input('Insira o número do grupo de planejamento: '))
            print()
            print('--------------------------------------------')
            print('Origens cadastradas: ')
            linhas, col = consultas.consulta_padrao(cur, 'origem')
            utils.imprimir_tabelas(linhas, col)
            origem = int(input('Insira o número da origem: '))

            cur.execute('INSERT INTO desp_fixa (descricao, dia, valor,'
                        ' categoria_id, grupo_id, origem_id) VALUES (?, ?, ?,'
                        ' ?, ?, ?)', (desc, dia, valor, categoria, grupo,
                                      origem))
            con.commit()
            print('Despesa fixa cadastrada com sucesso')
        else:
            break

        continua = utils.reiniciar_loop('despesas fixas')
        if continua == 'continue':
            continue
        else:
            print()
            break


# Função para cadastrar as receitas
def cadastro_receitas(con, cur):
    while True:
        os.system('cls')
        cabecalho = cabecalho_padrao + 'RECEITAS'
        utils.print_cabecalho(cabecalho)
        template = input('Deseja usar um template de receita já cadastrado?'
                         ' Digite S para Sim e N para Não: ').upper()

        if template == 'S':
            print()
            print('------------------------------------------------')
            print('Templates de receitas já cadastrados:')
            linha, col = consultas.consulta_padrao(cur, 'rec_templates')
            utils.imprimir_tabelas(linha, col)
            id_template = input('Insira o número do template desejado: ')
            rec, _ = consultas.consulta_com_where(cur, 'rec_templates', 'id',
                                                  id_template)
            desc = rec[0][1]
            valor = rec[0][2]
            data = rec[0][3]
        else:
            desc = input('Insira a descrição da receita: ')
            valor = float(input('Insira o valor da receita: '))
            data = int(input('Insira o dia da receita: '))

        year = int(input('Digite o ano do periodo que deseja usar no formato'
                         ' ##: '))
        year_str = str(year)
        consulta, _ = consultas.consulta_com_like(cur, '*', 'periodo',
                                                  'periodo', year_str)
        if consulta:
            print('Periodos cadastrados para o ano {}:'.format(year))
            linha, col = consultas.consulta_com_like(cur, '*', 'periodo',
                                                     'periodo', year_str)
            utils.imprimir_tabelas(linha, col)
        else:
            print('Ainda não há períodos cadastrados para o ano informado')

        per = input('Insira o número referente ao período de lançamento da'
                    ' receita: ')

        cur.execute('INSERT INTO receitas (descricao, data, valor, periodo_id)'
                    ' VALUES (?, ?, ?, ?)', (desc, data, valor, per))
        con.commit()
        print()
        print('Receita cadastrada com sucesso')
        print()
        print('--------------------------------------------------------------')
        print()
        print('Receitas já inseridas para este período:')
        linha, col = consultas.consulta_com_where(cur, 'receitas',
                                                  'periodo_id', per)
        utils.imprimir_tabelas(linha, col)
        continua = utils.reiniciar_loop('templates de receitas')
        if continua == 'continue':
            continue
        else:
            print()
            break


# Função para cadastrar as despesas
def cadastro_despesas(con, cur):
    while True:
        os.system('cls')
        cabecalho = cabecalho_padrao + 'DESPESAS POR PERÍODO'
        utils.print_cabecalho(cabecalho)
        ano = input('Para qual periodo deseja lançar a despesa? Informe o ano'
                    ' no formato ##: ')
        ano_str = str(ano)
        print()
        print('Periodos cadastrados para o ano {}:'.format(ano))
        periodo, col = consultas.consulta_com_like(cur, '*', 'periodo',
                                                   'periodo', ano_str)
        utils.imprimir_tabelas(periodo, col)
        print()
        per = input('Insira o número referente ao período desejado: ')
        os.system('cls')
        utils.print_cabecalho(cabecalho)
        cons_desp, _ = consultas.consulta_com_where(cur, 'despesas',
                                                    'periodo_id', per)
        per_completo = periodo[int(per) - 1][1]
        per_int = int(per)

        if not cons_desp:
            desp_fixa_input = input('Ainda não há despesas cadastradas para'
                                    ' este período. Deseja importar as'
                                    ' despesas fixas cadastradas? Digite S'
                                    ' para Sim e N para Não: ').upper()
            if desp_fixa_input == 'S':
                adiciona_desp_fixa_no_periodo(con, cur, per_completo, per_int)
        else:
            existe_fixa = False
            for linha in cons_desp:
                if linha[9] == 'FIXA':
                    existe_fixa = True
                    break
            if not existe_fixa:
                print('Despesas já cadastradas para este período:')
                linhas, col = consultas.consulta_padrao_com_inner_where(
                    cur, 'despesas', 'periodo_id', per)
                utils.imprimir_tabelas(linhas, col)
                print()
                desp_fixa_input = input(
                    'Ainda não há despesas fixas cadastradas para este'
                    ' período. Deseja importar as despesas fixas cadastradas?'
                    ' Digite S para Sim e N para Não: ').upper()

                if desp_fixa_input == 'S':
                    adiciona_desp_fixa_no_periodo(
                        con, cur, per_completo, per_int)

        print()
        print('Despesas já cadastradas para este período:')
        linhas, col = consultas.consulta_padrao_com_inner_where(
            cur, 'despesas', 'periodo_id', per)
        utils.imprimir_tabelas(linhas, col)
        print()
        confirm = input('Deseja cadastrar uma nova despesa? Digite S para Sim'
                        ' e N para Não: ').upper()

        if confirm == 'S':
            os.system('cls')
            utils.print_cabecalho(cabecalho)
            desc_lj = input('Insira o nome da despesa (loja): ')
            desc_desp = input('Insira uma descrição para a despesa: ')
            while True:
                data = input('Insira a data da despesa no formato DD/MM/'
                             'AAAA: ')

                try:
                    data_convertida = datetime.strptime(data, '%d/%m/%Y')
                    data_formatada = data_convertida.strftime('%d/%m/%Y')
                    break
                except ValueError:
                    print()
                    print('Data inválida. Digite a data no formato DD/MM/AAAA')

            while True:
                valor_in = input('Insira o valor da despesa: ').replace(',',
                                                                        '.')

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

            while True:
                tipo_in = input('Informe "f" se a despesa é fixa ou "v" se é'
                                ' variável: ').upper()

                if tipo_in == 'F':
                    tipo = 'FIXA'
                    break
                elif tipo_in == 'V':
                    tipo = 'VARIAVEL'
                    break
                else:
                    input('Opção inválida. Tecle ENTER para tentar novamente')
                    continue

            while True:
                num_parc = input(
                    'Informe o número de parcelas (zero para despesa única): ')
                try:
                    num_parc_int = int(num_parc)
                    if num_parc_int >= 0:
                        break
                except ValueError:
                    print('Número inválido. Insira um número inteiro positivo')
                    continue

            print('-----------------------------------------------')
            linhas, col = consultas.consulta_padrao(cur, 'categorias')
            utils.imprimir_tabelas(linhas, col)

            while True:
                categ = input('Selecione uma das categorias listadas acima: ')
                if categ.isdigit() and int(categ) in [linha[0] for linha in
                                                      linhas]:
                    break
                else:
                    print('Opção inválida. Selecione uma categoria válida')
                    continue

            print('-----------------------------------------------')
            linhas, col = consultas.consulta_padrao(cur, 'planejamento')
            utils.imprimir_tabelas(linhas, col)

            while True:
                grp_plan = input(
                    'Selecione um dos grupos de planejamento listados acima: ')
                if grp_plan.isdigit() and int(grp_plan) in [linha[0] for linha
                                                            in linhas]:
                    break
                else:
                    print('Opção inválida. Selecione um grupo de planejamento'
                          ' válido')
                    continue

            print('-----------------------------------------------')
            linhas, col = consultas.consulta_padrao(cur, 'origem')
            utils.imprimir_tabelas(linhas, col)

            while True:
                org_desp = input('Selecione uma das origens listadas acima: ')
                if org_desp.isdigit() and int(org_desp) in [linha[0] for linha
                                                            in linhas]:
                    break
                else:
                    print('Opção inválida. Selecione uma origem válida')
                    continue

            if num_parc == '0':
                num_parc_atual = num_parc
            else:
                num_parc_atual = '1'

            cur.execute("INSERT INTO despesas (desc_loja, desc_desp, data,"
                        " valor, tipo, parcelas_total, categoria_id, grupo_id,"
                        " origem_id, periodo_id, parcela_atual) VALUES (?, ?,"
                        " ?, ?, ?, ?, ?, ?, ?, ?, ?)",
                        (desc_lj, desc_desp, data_formatada, valor, tipo,
                         num_parc, categ, grp_plan, org_desp, per,
                         num_parc_atual))
            print()
            con.commit()
            print('Despesa cadastrada com sucesso')

            if num_parc != '0':
                print()
                print('------------------------------------------------')
                print()
                confirm = input('Deseja cadastrar as demais parcelas nos'
                                ' próximos períodos? Digite S para Sim e N'
                                ' para Não: ').upper()

                if confirm == 'S':
                    prx_per = per_int
                    for i in range(2, int(num_parc) + 1):
                        prx_per += 1
                        cur.execute("INSERT INTO despesas (desc_loja,"
                                    " desc_desp, data, valor, tipo,"
                                    " parcelas_total, categoria_id, grupo_id,"
                                    " origem_id, periodo_id, parcela_atual)"
                                    " VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?,"
                                    " ?)", (desc_lj, desc_desp, data_formatada,
                                            valor, tipo, num_parc, categ,
                                            grp_plan, org_desp, prx_per, i))
                    con.commit()
                    print()
                    print('Série de parcelas cadastrada com sucesso')
                else:
                    continua = utils.reiniciar_loop('despesas')
                    if continua == 'continue':
                        continue
                    else:
                        print()
                        break
        else:
            print()
            break

        continua = utils.reiniciar_loop('despesas')
        if continua == 'continue':
            continue
        else:
            print()
            break


def adiciona_desp_fixa_no_periodo(con, cur, per_completo, per_int):
    desp_fixas, _ = consultas.consulta_padrao(cur, 'desp_fixa')
    for linha in desp_fixas:
        data_completa = (str(linha[2]) + '/' + per_completo)
        data_convertida = datetime.strptime(data_completa,
                                            '%d/%b/%y')
        data_formatada = data_convertida.strftime('%d/%m/%Y')
        cur.execute("INSERT INTO despesas (desc_loja, desc_desp, data, valor,"
                    " categoria_id, parcela_atual, parcelas_total, grupo_id,"
                    " tipo, origem_id, periodo_id) VALUES (?, '', ?, ?, ?, 0,"
                    " 0, ?, 'FIXA', ?, ?)", (linha[1], data_formatada,
                                             linha[4], linha[3], linha[5],
                                             linha[6], per_int))
    con.commit()
    print()
    print('Despesas fixas inseridas com sucesso no período ', per_completo)
    print()
