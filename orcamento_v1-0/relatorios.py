# Função para gerar relatório de despesas por categoria com soma e agrupamento
def rel_categorias(cur, coluna_cat, coluna_soma, tabela, periodo):
    resultado = cur.execute(f'SELECT {coluna_cat}, SUM({coluna_soma})'
                            f' FROM {tabela} WHERE periodo_id={periodo}'
                            f' GROUP BY {coluna_cat}').fetchall()
    return resultado


# Função para gerar soma de todas as despesas de um período informado
def rel_soma_geral(cur, coluna_soma, tabela, periodo):
    resultado = cur.execute(f'SELECT SUM({coluna_soma})'
                            f' FROM {tabela} WHERE periodo_id={periodo}'
                            ).fetchone()
    return resultado[0] if resultado[0] is not None else 0
