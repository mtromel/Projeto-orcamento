"""
Autor: Marcos Cristiano Trömel
Data: 09/04/2025
Descrição: Sistema de Orçamento Pessoal

Permite o cadastro, consulta, alteração e exclusão de despesas, categorias,
grupo de planejamento, despesas fixas, receitas, templates de receitas e
origens de despesas. Além disso, possibilita a geração de relatórios de
despesas e receitas filtrando por período, agrupando por categoria ou grupo de
planejamento. Os grupos de planejamento seguem o método de planejamento
financeiro do 'Me Poupe' que é dividido em 5 grupos: Essencial (55% do total
das receitas), Educação (5% do total das receitas), Objetivos (20% do total
das receitas), Aposentadoria (10% do total das receitas) e Gastar (10% do total
das receitas).
"""

import insere
import utils
import os
import consultas
import alterar
import deletar
import relatorios
import create_bd_orcamento
import sqlite3
from pathlib import Path


THIS_FOLDER = Path(__file__).parent.resolve()
con, cur = utils.conectar_bd(THIS_FOLDER / 'bd_orcamento.db')


# Consulta se o banco de dados existe, caso contrário, cria o banco de dados
cons = os.path.exists('bd_orcamento.db')
if not cons:
    try:
        create_bd_orcamento.create_bd
    except sqlite3.Error:
        print('Erro ao criar o banco de dados.')


while True:
    # Limpa a tela e imprime o menu principal do sistema
    os.system('cls')
    utils.print_cabecalho('SISTEMA DE ORÇAMENTO PESSOAL')
    print()
    print('1 - CADASTRAR')
    print('2 - CONSULTAR')
    print('3 - ALTERAR')
    print('4 - EXCLUIR')
    print('5 - RELATÓRIOS')
    print('6 - SAIR')
    opcao = input('SELECIONE A OPÇÃO DESEJADA: ')

    match opcao:
        case '1':
            # Limpa a tela e imprime o menu de cadastros
            os.system('cls')
            utils.print_cabecalho('CADASTROS')
            print()
            print('1 - CADASTRAR DESPESAS')
            print('2 - CADASTRAR PERÍODOS')
            print('3 - CADASTRAR CATEGORIAS')
            print('4 - CADASTRAR DESPESAS FIXAS')
            print('5 - CADASTRAR ORIGENS')
            print('6 - CADASTRAR RECEITAS')
            print('7 - CADASTRAR TEMPLATES DE RECEITAS')
            print('8 - VOLTAR')
            opcao_cad = input('SELECIONE A OPÇÃO DESEJADA: ')
            match opcao_cad:
                case '1':
                    # Chama a função de cadastro de despesas
                    insere.cadastro_despesas()
                    continue
                case '2':
                    # Chama a função de cadastro de períodos de despesas
                    insere.cadastro_periodo()
                    continue
                case '3':
                    # Chama a função de cadastro de categorias de despesas
                    insere.cadastra_categorias()
                    continue
                case '4':
                    # Chama a função de cadastro de despesas fixas
                    insere.cadastro_despesas_fixas()
                    continue
                case '5':
                    # Chama a função de cadastro de origens de despesas
                    insere.cadastro_origens()
                    continue
                case '6':
                    # Chama a função de cadastro de receitas
                    insere.cadastro_receitas()
                    continue
                case '7':
                    # Chama a função de cadastro de templates de receitas
                    insere.cadastro_templates_receitas()
                    continue
                case '8':
                    # Retorna ao menu principal
                    continue
                case _:
                    # Captura opção inválida e informa ao usuário retornando
                    # ao menu principal
                    os.system('cls')
                    utils.print_cabecalho('CADASTROS')
                    print()
                    input('Opção inválida. Tente novamente.')
                    continue
        case '2':
            # Limpa a tela e imprime o menu de consultas
            os.system('cls')
            utils.print_cabecalho('CONSULTAS')
            print()
            print('1 - CONSULTAR DESPESAS CADASTRADAS')
            print('2 - CONSULTAR PERÍODOS CADASTRADOS')
            print('3 - CONSULTAR CATEGORIAS CADASTRADAS')
            print('4 - CONSULTAR GRUPOS DE PLANEJAMENTO CADASTRADOS')
            print('5 - CONSULTAR DESPESAS FIXAS CADASTRADAS')
            print('6 - CONSULTAR ORIGENS CADASTRADAS')
            print('7 - CONSULTAR RECEITAS CADASTRADAS')
            print('8 - CONSULTAR TEMPLATES DE RECEITAS CADASTRADAS')
            print('9 - VOLTAR')
            opcao_cad = input('SELECIONE A OPÇÃO DESEJADA: ')
            match opcao_cad:
                case '1':
                    # Chama a função de consulta de despesas cadastradas
                    # por período
                    os.system('cls')
                    utils.print_cabecalho('LISTA DAS DESPESAS CADASTRADAS')
                    per = input('Informe o período que deseja consultar: ')
                    print()
                    consultas.consulta_padrao_com_inner_where(cur, 'despesas',
                                                              'periodo_id',
                                                              per)
                    input('Pressione ENTER para continuar...')
                case '2':
                    # Chama a função de consulta de períodos cadastrados
                    os.system('cls')
                    utils.print_cabecalho('LISTA DOS PERÍODOS CADASTRADOS')
                    consultas.consulta_padrao(cur, 'periodo')
                    input('Pressione ENTER para continuar...')
                case '3':
                    # Chama a função de consulta de categorias cadastradas
                    os.system('cls')
                    utils.print_cabecalho('LISTA DAS CATEGORIAS CADASTRADAS')
                    consultas.consulta_padrao(cur, 'categorias')
                    input('Pressione ENTER para continuar...')
                case '4':
                    # Chama a função de consulta de grupos de planejamento
                    # cadastrados
                    os.system('cls')
                    utils.print_cabecalho('LISTA DOS GRUPOS DE PLANEJAMENTO'
                                          ' CADASTRADOS')
                    consultas.consulta_padrao(cur, 'planejamento')
                    input('Pressione ENTER para continuar...')
                case '5':
                    # Chama a função de consulta de despesas fixas cadastradas
                    os.system('cls')
                    utils.print_cabecalho('LISTA DAS DESPESAS FIXAS'
                                          ' CADASTRADAS')
                    consultas.consulta_padrao_com_inner(cur, 'desp_fixa')
                    input('Pressione ENTER para continuar...')
                case '6':
                    # Chama a função de consulta de origens cadastradas
                    os.system('cls')
                    utils.print_cabecalho('LISTA DAS ORIGENS CADASTRADAS')
                    consultas.consulta_padrao(cur, 'origem')
                    input('Pressione ENTER para continuar...')
                case '7':
                    # Chama a função de consulta de receitas cadastradas
                    # por período
                    os.system('cls')
                    utils.print_cabecalho('LISTA DAS RECEITAS CADASTRADAS')
                    per = input('Informe o período que deseja consultar: ')
                    print()
                    consultas.consulta_padrao_com_inner_where(cur, 'receitas',
                                                              'periodo_id',
                                                              per)
                    input('Pressione ENTER para continuar...')
                case '8':
                    # Chama a função de consulta de templates de receitas
                    # cadastradas
                    os.system('cls')
                    utils.print_cabecalho('LISTA DOS TEMPLATES DE RECEITAS'
                                          ' CADASTRADAS')
                    consultas.consulta_padrao(cur, 'rec_templates')
                    input('Pressione ENTER para continuar...')
                case '9':
                    # Retorna ao menu principal
                    continue
                case _:
                    # Captura opção inválida e informa ao usuário retornando
                    # ao menu principal
                    os.system('cls')
                    utils.print_cabecalho('CONSULTAS')
                    print()
                    input('Opção inválida. Tente novamente.')
                    continue
        case '3':
            # Limpa a tela e imprime o menu de alterações
            os.system('cls')
            utils.print_cabecalho('ALTERAÇÕES')
            print()
            print('1 - ALTERAR DESPESAS CADASTRADAS')
            print('2 - ALTERAR CATEGORIAS CADASTRADAS')
            print('3 - ALTERAR GRUPOS DE PLANEJAMENTO CADASTRADOS')
            print('4 - ALTERAR DESPESAS FIXAS CADASTRADAS')
            print('5 - ALTERAR ORIGENS CADASTRADAS')
            print('6 - ALTERAR RECEITAS CADASTRADAS')
            print('7 - ALTERAR TEMPLATES DE RECEITAS CADASTRADAS')
            print('8 - VOLTAR')
            opcao_cad = input('SELECIONE A OPÇÃO DESEJADA: ')
            match opcao_cad:
                case '1':
                    # Chama a função de alteração de despesas cadastradas
                    # por período
                    os.system('cls')
                    utils.print_cabecalho('LISTA DAS DESPESAS CADASTRADAS')
                    per = input(
                        'Informe o período que deseja alterar um lançamento: ')
                    print()
                    # Consulta as despesas cadastradas no período informado
                    # e imprime na tela
                    consultas.consulta_com_where(
                        cur, 'despesas', 'periodo_id', per)
                    # Carrega em memória as despesas cadastradas no período
                    # informado sem imprimir na tela
                    listagem = consultas.consulta_com_where_sem_imprimir(
                        cur, '*', 'despesas', 'periodo_id', per)
                    if listagem:
                        desp = input(
                            'Informe o id da despesa que deseja alterar: ')
                        if desp not in [str(linha[0]) for linha in listagem]:
                            print('Id informado não encontrado.')
                            input('Pressione ENTER para continuar...')
                        else:
                            os.system('cls')
                            consultas.consulta_com_where(
                                cur, 'despesas', 'id', desp)
                            alterar.alterar_despesa(con, cur, per, desp)
                    else:
                        print('Nenhum registro encontrado para o período'
                              ' informado.')
                        input('Pressione ENTER para continuar...')
                case '2':
                    # Chama a função de alteração de categorias cadastradas
                    os.system('cls')
                    utils.print_cabecalho('LISTA DAS CATEGORIAS CADASTRADAS')
                    # Consulta as categorias cadastradas e imprime na tela
                    consultas.consulta_padrao(cur, 'categorias')
                    # Carrega em memória as categorias cadastradas sem
                    # imprimir na tela
                    listagem = consultas.consulta_padrao_sem_imprimir(
                        cur, 'categorias')
                    id_cat = input(
                        'Insira o id da categoria que deseja alterar: ')
                    if listagem:
                        if id_cat not in [str(linha[0]) for linha in listagem]:
                            print('ID informado não encontrado.')
                            input('Pressione ENTER para continuar...')
                        else:
                            os.system('cls')
                            consultas.consulta_com_where(
                                cur, 'categorias', 'id', id_cat)
                            alterar.alterar_categoria(cur, con, id_cat)
                    else:
                        print('Nenhum registro encontrado.')
                        input('Pressione ENTER para continuar...')
                case '3':
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
                case '4':
                    # Chama a função de alteração de despesas fixas cadastradas
                    os.system('cls')
                    utils.print_cabecalho(
                        'LISTA DAS DESPESAS FIXAS CADASTRADAS')

                    # Consulta as despesas fixas cadastradas e imprime na tela
                    consultas.consulta_padrao(cur, 'desp_fixa')

                    # Carrega em memória as despesas fixas cadastradas sem
                    # imprimir na tela
                    listagem = consultas.consulta_padrao_sem_imprimir(
                        cur, 'desp_fixa')
                    id_desp_fixa = input(
                        'Insira o id da despesa fixa que deseja alterar: ')
                    if listagem:
                        if id_desp_fixa not in [str(linha[0]) for linha in
                                                listagem]:
                            print('ID informado não encontrado.')
                            input('Pressione ENTER para continuar...')
                        else:
                            os.system('cls')
                            consultas.consulta_com_where(
                                cur, 'desp_fixa', 'id', id_desp_fixa)
                            alterar.alterar_desp_fixa(cur, con, id_desp_fixa)
                    else:
                        print('Nenhum registro encontrado.')
                        input('Pressione ENTER para continuar...')
                case '5':
                    # Chama a função de alteração de origens cadastradas
                    os.system('cls')
                    utils.print_cabecalho('LISTA DAS ORIGENS CADASTRADAS')

                    # Consulta as origens cadastradas e imprime na tela
                    consultas.consulta_padrao(cur, 'origem')

                    # Carrega em memória as origens cadastradas sem
                    # imprimir na tela
                    listagem = consultas.consulta_padrao_sem_imprimir(
                        cur, 'origem')
                    id_org = input(
                        'Insira o id da origem que deseja alterar: ')
                    if listagem:
                        if id_org not in [str(linha[0]) for linha in listagem]:
                            print('ID informado não encontrado.')
                            input('Pressione ENTER para continuar...')
                        else:
                            os.system('cls')
                            consultas.consulta_com_where(
                                cur, 'origem', 'id', id_org)
                            alterar.alterar_origem(cur, con, id_org)
                    else:
                        print('Nenhum registro encontrado.')
                        input('Pressione ENTER para continuar...')
                case '6':
                    # Chama a função de alteração de receitas cadastradas
                    # por período
                    os.system('cls')
                    utils.print_cabecalho('LISTA DAS RECEITAS CADASTRADAS')
                    per = input(
                        'Informe o período que deseja alterar um lançamento: ')
                    print()

                    # Consulta as receitas cadastradas no período informado
                    # e imprime na tela
                    consultas.consulta_com_where(
                        cur, 'receitas', 'periodo_id', per)

                    # Carrega em memória as receitas cadastradas no período
                    # informado sem imprimir na tela
                    listagem = consultas.consulta_com_where_sem_imprimir(
                        cur, '*', 'receitas', 'periodo_id', per)
                    if listagem:
                        rece = input(
                            'Informe o id da despesa que deseja alterar: ')
                        if rece not in [str(linha[0]) for linha in listagem]:
                            print('Id informado não encontrado.')
                            input('Pressione ENTER para continuar...')
                        else:
                            os.system('cls')
                            consultas.consulta_com_where(
                                cur, 'receitas', 'id', rece)
                            alterar.alterar_receitas(con, cur, per, rece)
                    else:
                        print('Nenhum registro encontrado para o período'
                              ' informado.')
                        input('Pressione ENTER para continuar...')
                case '7':
                    # Chama a função de alteração de templates de receitas
                    # cadastradas
                    os.system('cls')
                    utils.print_cabecalho(
                        'LISTA DOS TEMPLATES DE RECEITAS CADASTRADAS')

                    # Consulta os templates de receitas cadastradas e
                    # imprime na tela
                    consultas.consulta_padrao(cur, 'rec_templates')

                    # Carrega em memória os templates de receitas cadastradas
                    # sem imprimir na tela
                    listagem = consultas.consulta_padrao_sem_imprimir(
                        cur, 'rec_templates')
                    id_tpl = input(
                        'Insira o id do template que deseja alterar: ')
                    if listagem:
                        if id_tpl not in [str(linha[0]) for linha in listagem]:
                            print('ID informado não encontrado.')
                            input('Pressione ENTER para continuar...')
                        else:
                            os.system('cls')
                            consultas.consulta_com_where(
                                cur, 'rec_templates', 'id', id_tpl)
                            alterar.alterar_rec_templates(con, cur, id_tpl)
                    else:
                        print('Nenhum registro encontrado.')
                        input('Pressione ENTER para continuar...')
                case '8':
                    # Retorna ao menu principal
                    continue
                case _:
                    # Captura opção inválida e informa ao usuário retornando
                    # ao menu principal
                    os.system('cls')
                    utils.print_cabecalho('LISTA DAS DESPESAS CADASTRADAS')
                    print()
                    input('Opção inválida. Tente novamente.')
                    continue
        case '4':
            # Limpa a tela e imprime o menu de exclusões
            os.system('cls')
            utils.print_cabecalho('APAGAR REGISTROS')
            print()
            print('1 - APAGAR DESPESAS CADASTRADAS')
            print('2 - APAGAR PERÍODOS CADASTRADOS')
            print('3 - APAGAR CATEGORIAS CADASTRADAS')
            print('4 - APAGAR GRUPOS DE PLANEJAMENTO CADASTRADOS')
            print('5 - APAGAR DESPESAS FIXAS CADASTRADAS')
            print('6 - APAGAR ORIGENS CADASTRADAS')
            print('7 - APAGAR RECEITAS CADASTRADAS')
            print('8 - APAGAR TEMPLATES DE RECEITAS CADASTRADAS')
            print('9 - VOLTAR')
            opcao_cad = input('SELECIONE A OPÇÃO DESEJADA: ')
            match opcao_cad:
                case '1':
                    # Chama a função de exclusão apropriada para despesas
                    # cadastradas
                    os.system('cls')
                    utils.print_cabecalho('LISTA DE DESPESAS')

                    # Consulta as despesas cadastradas e imprime na tela
                    consultas.consulta_padrao(cur, 'despesas')
                    tipo = input('Deseja apagar um registro apenas? Digite'
                                 ' 1.\n'
                                 'Deseja apagar todos os registros da tabela?'
                                 ' Digite 2. \n'
                                 'Deseja apagar todos os registros de um'
                                 ' período? Digite 3. \n'
                                 ' SELECIONE A OPÇÃO DESEJADA: ')
                    if tipo == '1':
                        deletar.apagar_registro(con, cur, 'despesas')
                    elif tipo == '2':
                        deletar.apagar_todos_registros(con, cur, 'despesas')
                    elif tipo == '3':
                        deletar.apagar_todos_reg_com_where(
                            con, cur, 'despesas', 'periodo_id', input(
                                'Informe o id do período que deseja apagar: '))
                    else:
                        input('Opção inválida, tente novamente. Pressione'
                              ' ENTER para continuar')
                case '2':
                    # Chama a função de exclusão apropriada para períodos
                    # cadastrados
                    os.system('cls')
                    utils.print_cabecalho('LISTA DE PERÍODOS')

                    # Consulta os períodos cadastrados e imprime na tela
                    consultas.consulta_padrao(cur, 'periodo')
                    tipo = input('Deseja apagar um registro apenas? Digite'
                                 ' 1.\n'
                                 'Deseja apagar todos os registros da tabela?'
                                 ' Digite 2. \n'
                                 'SELECIONE A OPÇÃO DESEJADA: ')
                    if tipo == '1':
                        deletar.apagar_registro(con, cur, 'periodo')
                    elif tipo == '2':
                        deletar.apagar_todos_registros(con, cur, 'periodo')
                    else:
                        input('Opção inválida, tente novamente. Pressione'
                              ' ENTER para continuar')
                case '3':
                    # Chama a função de exclusão apropriada para categorias
                    os.system('cls')
                    utils.print_cabecalho('LISTA DE CATEGORIAS')

                    # Consulta as categorias cadastradas e imprime na tela
                    consultas.consulta_padrao(cur, 'categorias')
                    tipo = input('Deseja apagar um registro apenas? Digite'
                                 ' 1.\n'
                                 'Deseja apagar todos os registros da tabela?'
                                 ' Digite 2. \n'
                                 'SELECIONE A OPÇÃO DESEJADA: ')
                    if tipo == '1':
                        deletar.apagar_registro(con, cur, 'categorias')
                    elif tipo == '2':
                        deletar.apagar_todos_registros(con, cur, 'categorias')
                    else:
                        input('Opção inválida, tente novamente. Pressione'
                              ' ENTER para continuar')
                case '4':
                    # Chama a função de exclusão apropriada para grupos de
                    # planejamento cadastrados
                    os.system('cls')
                    utils.print_cabecalho('LISTA DE GRUPOS DE PLANEJAMENTO')

                    # Consulta os grupos de planejamento cadastrados e imprime
                    # na tela
                    consultas.consulta_padrao(cur, 'planejamento')
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
                case '5':
                    # Chama a função de exclusão apropriada para despesas
                    # fixas cadastradas
                    os.system('cls')
                    utils.print_cabecalho('LISTA DE DESPESAS FIXAS')

                    # Consulta as despesas fixas cadastradas e imprime na tela
                    consultas.consulta_padrao(cur, 'desp_fixa')
                    tipo = input('Deseja apagar um registro apenas? Digite'
                                 ' 1.\n'
                                 'Deseja apagar todos os registros da tabela?'
                                 ' Digite 2. \n'
                                 'SELECIONE A OPÇÃO DESEJADA: ')
                    if tipo == '1':
                        deletar.apagar_registro(con, cur, 'desp_fixa')
                    elif tipo == '2':
                        deletar.apagar_todos_registros(con, cur, 'desp_fixa')
                    else:
                        input('Opção inválida, tente novamente. Pressione'
                              ' ENTER para continuar')
                case '6':
                    # Chama a função de exclusão apropriada para origens
                    # cadastradas
                    os.system('cls')
                    utils.print_cabecalho('LISTA DE ORIGENS')

                    # Consulta as origens cadastradas e imprime na tela
                    consultas.consulta_padrao(cur, 'origem')
                    tipo = input('Deseja apagar um registro apenas? Digite'
                                 ' 1.\n'
                                 'Deseja apagar todos os registros da tabela?'
                                 ' Digite 2. \n'
                                 'SELECIONE A OPÇÃO DESEJADA: ')
                    if tipo == '1':
                        deletar.apagar_registro(con, cur, 'origem')
                    elif tipo == '2':
                        deletar.apagar_todos_registros(con, cur, 'origem')
                    else:
                        input('Opção inválida, tente novamente. Pressione'
                              ' ENTER para continuar')
                case '7':
                    # Chama a função de exclusão apropriada para receitas
                    # cadastradas
                    os.system('cls')
                    utils.print_cabecalho('LISTA DE RECEITAS')

                    # Consulta as receitas cadastradas e imprime na tela
                    consultas.consulta_padrao(cur, 'receitas')
                    tipo = input('Deseja apagar um registro apenas? Digite'
                                 ' 1.\n'
                                 'Deseja apagar todos os registros da tabela?'
                                 ' Digite 2. \n'
                                 'Deseja apagar todos os registros de um'
                                 ' período? Digite 3. \n'
                                 ' SELECIONE A OPÇÃO DESEJADA: ')
                    if tipo == '1':
                        deletar.apagar_registro(con, cur, 'receitas')
                    elif tipo == '2':
                        deletar.apagar_todos_registros(con, cur, 'receitas')
                    elif tipo == '3':
                        deletar.apagar_todos_reg_com_where(
                            con, cur, 'receitas', 'periodo_id', input(
                                'Informe o id do período que deseja apagar: '))
                    else:
                        input('Opção inválida, tente novamente. Pressione'
                              ' ENTER para continuar')
                case '8':
                    # Chama a função de exclusão apropriada para templates de
                    # receitas cadastradas
                    os.system('cls')
                    utils.print_cabecalho('LISTA DE TEMPLATES DE RECEITAS')

                    # Consulta os templates de receitas cadastradas e imprime
                    # na tela
                    consultas.consulta_padrao(cur, 'rec_templates')
                    tipo = input('Deseja apagar um registro apenas? Digite'
                                 ' 1.\n'
                                 'Deseja apagar todos os registros da tabela?'
                                 ' Digite 2. \n'
                                 'SELECIONE A OPÇÃO DESEJADA: ')
                    if tipo == '1':
                        deletar.apagar_registro(con, cur, 'rec_templates')
                    elif tipo == '2':
                        deletar.apagar_todos_registros(
                            con, cur, 'rec_templates')
                    else:
                        input('Opção inválida, tente novamente. Pressione'
                              ' ENTER para continuar')
                case '9':
                    # Retorna ao menu principal
                    continue
                case _:
                    # Captura opção inválida e informa ao usuário retornando
                    os.system('cls')
                    utils.print_cabecalho('LISTA DE DESPESAS')
                    print()
                    input('Opção inválida. Tente novamente.')
                    continue
        case '5':
            # Limpa a tela e imprime o menu de relatórios
            os.system('cls')
            utils.print_cabecalho('RELATÓRIOS')
            print()
            print('1 - RELATORIO TOTAL POR CATEGORIA POR PERÍODO')
            print('2 - RELATORIO TOTAL POR GRUPO DE PLANEJAMENTO POR PERÍODO')
            print('3 - ORÇAMENTO MENSAL POR PERÍODO')
            print('4 - RELATORIO TOTAL POR ORIGEM DE DESPESAS POR PERÍODO')
            print('5 - VOLTAR')
            opcao_cad = input('SELECIONE A OPÇÃO DESEJADA: ')
            match opcao_cad:
                case '1':
                    # Chama a função de relatório total por categoria por
                    # período
                    os.system('cls')
                    utils.print_cabecalho('TOTAL POR CATEGORIA POR PERIODO')
                    per = input('Informe o período que deseja consultar: ')
                    print()

                    # Carrega em memória o resultado do relatório de categorias
                    # no período informado somando os valores de despesas
                    # agrupando por categoria
                    resultado = relatorios.rel_categorias(
                        cur, 'categoria_id', 'valor', 'despesas', per)

                    # Carrega em memória as categorias
                    categorias = consultas.consulta_padrao_sem_imprimir(
                        cur, 'categorias')

                    # Carrega em memória a descrição do período informado
                    periodo = consultas.consulta_com_where_sem_imprimir(
                        cur, 'periodo', 'periodo', 'id', per)
                    print()
                    print('-' * 40)
                    print(f'Despesas do período {per} - {periodo[0][0]}')
                    print()
                    for linha in resultado:
                        print(f'{categorias[int(linha[0]) - 1][1]}:'
                              f' R$ {linha[1]:.2f}')
                    print()
                    print('-' * 40)
                    print()
                    input('Pressione ENTER para continuar...')
                case '2':
                    # Chama a função de relatório total por grupo de
                    # planejamento por período
                    os.system('cls')
                    utils.print_cabecalho(
                        'TOTAL POR GRUPO DE PLANEJAMENTO POR PERIODO')
                    per = input('Informe o período que deseja consultar: ')
                    print()

                    # Carrega em memória o resultado do relatório de categorias
                    # no período informado somando os valores de despesas
                    # agrupando por grupo de planejamento
                    resultado = relatorios.rel_categorias(
                        cur, 'grupo_id', 'valor', 'despesas', per)

                    # Carrega em memória os grupos de planejamento
                    categorias = consultas.consulta_padrao_sem_imprimir(
                        cur, 'planejamento')

                    # Carrega em memória a descrição do período informado
                    periodo = consultas.consulta_com_where_sem_imprimir(
                        cur, 'periodo', 'periodo', 'id', per)
                    print()
                    print('-' * 40)
                    print(f'Despesas do período {per} - {periodo[0][0]}')
                    print()
                    for linha in resultado:
                        if linha[0] == '':
                            print(' ')
                        else:
                            print(f'{categorias[int(linha[0]) - 1][1]}:'
                                  f' R$ {linha[1]:.2f}')
                    print()
                    print('-' * 40)
                    print()
                    input('Pressione ENTER para continuar...')
                case '3':
                    # Chama a função de relatório que exibe o orçamento mensal
                    # por período
                    total = 0
                    os.system('cls')
                    utils.print_cabecalho('ORÇAMENTO MENSAL POR PERIODO')
                    per = input('Informe o período que deseja consultar: ')

                    # Carrega em memória o resultado do relatório de categorias
                    # no período informado somando os valores de despesas
                    # agrupando por grupo de planejamento
                    resultado = relatorios.rel_categorias(
                        cur, 'grupo_id', 'valor', 'despesas', per)

                    # Carrega em memória o resultado do relatório de categorias
                    # no período informado somando os valores de despesas
                    # agrupando por categoria
                    resultado2 = relatorios.rel_categorias(
                        cur, 'categoria_id', 'valor', 'despesas', per)

                    # Carrega em memória os grupos de planejamento
                    categorias = consultas.consulta_padrao_sem_imprimir(
                        cur, 'planejamento')

                    # Carrega em memória as categorias
                    categorias2 = consultas.consulta_padrao_sem_imprimir(
                        cur, 'categorias')

                    # Carrega em memória a descrição do período informado
                    periodo = consultas.consulta_com_where_sem_imprimir(
                        cur, 'periodo', 'periodo', 'id', per)

                    # Carrega em memória o valor total de receitas do período
                    # informado
                    receitas = relatorios.rel_soma_geral(
                        cur, 'valor', 'receitas', per)

                    print('-' * 40)
                    print(f'Orçamento mensal do período {per} -'
                          f' {periodo[0][0]}')
                    print()
                    print('-' * 20)
                    print(f'Receitas: R$ {receitas:.2f}')
                    print('-' * 20)
                    print()
                    print('Despesas por grupo de planejamento: ')
                    print('-' * 42)
                    print('    GRUPO          $ ALVO      $ REALIZADO')
                    print('-' * 42)
                    for linha in resultado:
                        if linha[0] == '':
                            print(' ')
                        else:
                            taxa = 0.0
                            tam = (14-(len(categorias[int(linha[0]) - 1][1])))

                            # Verifica a categoria do grupo de planejamento e
                            # atribui a taxa correspondente de acordo com o
                            # método 'Me Poupe'
                            if categorias[int(linha[0]) - 1][1] == 'Essencial':
                                taxa = 0.55
                            elif (categorias[int(linha[0]) - 1][1] ==
                                  'Educação'):
                                taxa = 0.05
                            elif (categorias[int(linha[0]) - 1][1] ==
                                  'Objetivos'):
                                taxa = 0.20
                            elif (categorias[int(linha[0]) - 1][1] ==
                                  'Aposentadoria'):
                                taxa = 0.10
                            elif categorias[int(linha[0]) - 1][1] == 'Gastar':
                                taxa = 0.10
                            print(f'    {categorias[int(linha[0]) - 1][1]}:',
                                  end='')
                            print(' ' * tam, end='')
                            print(f'R$ {(receitas * taxa):.2f}', end='')
                            if ((receitas * taxa) < 1000 and (receitas * taxa
                                                              ) >= 100):
                                print(f'   R$ {linha[1]:.2f}')
                            elif (receitas * taxa) < 100:
                                print(f'    R$ {linha[1]:.2f}')
                            elif (receitas * taxa) >= 1000:
                                print(f'  R$ {linha[1]:.2f}')
                            total += linha[1]

                    print('Despesas por categoria: ')
                    print('-' * 27)
                    print('    CATEGORIA         VALOR')
                    print('-' * 27)
                    for linha in resultado2:
                        tam = (18 - (len(categorias2[int(linha[0]) - 1][1])))
                        print(f'    {categorias2[int(linha[0]) - 1][1]}:',
                              end='')
                        print(' ' * tam, end='')
                        print(f'R$ {linha[1]:.2f}')

                    print()
                    print('-' * 20)
                    print(f'Saldo: R$ {receitas - total:.2f}')
                    print('-' * 20)

                    print()
                    input('Pressione ENTER para continuar...')
                case '4':
                    # Chama a função de relatório total por origem de despesas
                    # por período
                    os.system('cls')
                    utils.print_cabecalho(
                        'TOTAL POR ORIGEM DE DESPESAS POR PERIODO')
                    per = input('Informe o período que deseja consultar: ')
                    print()

                    # Carrega em memória o resultado do relatório de total
                    # de despesas por origem no período informado.
                    resultado = relatorios.rel_categorias(
                        cur, 'origem_id', 'valor', 'despesas', per)

                    # Carrega em memória as origens cadastradas
                    categorias = consultas.consulta_padrao_sem_imprimir(
                        cur, 'origem')

                    # Carrega em memória a descrição do período informado
                    periodo = consultas.consulta_com_where_sem_imprimir(
                        cur, 'periodo', 'periodo', 'id', per)
                    print()
                    print('-' * 40)
                    print(f'Despesas do período {per} - {periodo[0][0]}')
                    print()
                    for linha in resultado:
                        if linha[0] == '':
                            print(' ')
                        else:
                            print(f'{categorias[int(linha[0]) - 1][1]}:'
                                  f' R$ {linha[1]:.2f}')
                    print()
                    print('-' * 40)
                    print()
                    input('Pressione ENTER para continuar...')
                case '5':
                    # Retorna ao menu principal
                    continue
                case _:
                    # Captura opção inválida e informa ao usuário retornando
                    # ao menu principal
                    os.system('cls')
                    utils.print_cabecalho('RELATÓRIOS')
                    print()
                    input('Opção inválida. Tente novamente.')
                    continue
        case '6':
            # Fecha a conexão do banco de dados e encerra o programa
            con.close()
            break
        case _:
            # Captura opção inválida e informa ao usuário retornando ao menu
            # principal
            os.system('cls')
            utils.print_cabecalho('SISTEMA DE ORÇAMENTO PESSOAL')
            print()
            input('Opção inválida. Tente novemnte.')
            continue
