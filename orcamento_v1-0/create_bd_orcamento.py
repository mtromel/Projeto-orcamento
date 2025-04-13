import sqlite3


con = sqlite3.connect('bd_orcamento.db')
cur = con.cursor()


# Cria o banco de dados e as tabelas necessárias para o funcionamento do
# sistema de controle de orçamento pessoal.
def create_bd():
    cur.execute('CREATE TABLE IF NOT EXISTS categorias (id INTEGER PRIMARY'
                ' KEY AUTOINCREMENT UNIQUE NOT NULL, categoria VARCHAR(20))')
    cur.execute('CREATE TABLE IF NOT EXISTS planejamento (id INTEGER PRIMARY'
                ' KEY AUTOINCREMENT UNIQUE NOT NULL, grupo VARCHAR(20))')
    cur.execute('CREATE TABLE IF NOT EXISTS origem(id INTEGER PRIMARY KEY'
                ' AUTOINCREMENT UNIQUE NOT NULL, origem VARCHAR(20))')
    cur.execute('CREATE TABLE IF NOT EXISTS periodo (id INTEGER PRIMARY KEY'
                ' AUTOINCREMENT UNIQUE NOT NULL, periodo VARCHAR(7))')
    cur.execute('CREATE TABLE IF NOT EXISTS despesas (id INTEGER PRIMARY KEY'
                ' AUTOINCREMENT UNIQUE NOT NULL, desc_loja VARCHAR(50),'
                ' desc_desp VARCHAR(50), data DATE, valor REAL, categoria_id'
                ' INTEGER, parcela_atual INTEGER, parcelas_total INTEGER,'
                ' grupo_id INTEGER, tipo VARCHAR(9), origem_id INTEGER,'
                ' periodo_id INTEGER, FOREIGN KEY(categoria_id) REFERENCES'
                ' categorias(id), FOREIGN KEY(grupo_id) REFERENCES'
                ' planejamento(id), FOREIGN KEY(origem_id) REFERENCES'
                ' origem(id), FOREIGN KEY(periodo_id) REFERENCES periodo(id))')
    cur.execute('CREATE TABLE IF NOT EXISTS desp_fixa (id INTEGER PRIMARY KEY'
                ' AUTOINCREMENT UNIQUE NOT NULL, descricao VARCHAR(20), dia'
                ' INTEGER, categoria_id INTEGER, valor REAL, grupo_id INTEGER,'
                ' origem_id INTEGER,'
                ' FOREIGN KEY(categoria_id) REFERENCES categorias(id),'
                ' FOREIGN KEY(grupo_id) REFERENCES planejamento(id),'
                ' FOREIGN KEY(origem_id) REFERENCES origem(id))')
    cur.execute('CREATE TABLE IF NOT EXISTS rec_templates (id INTEGER PRIMARY'
                ' KEY AUTOINCREMENT UNIQUE NOT NULL, descricao VARCHAR(20),'
                ' valor REAL, data DATE)')
    cur.execute('CREATE TABLE IF NOT EXISTS receitas (id INTEGER PRIMARY KEY'
                ' AUTOINCREMENT UNIQUE NOT NULL, descricao VARCHAR(20), data'
                ' DATE, valor REAL, periodo_id INTEGER, FOREIGN'
                ' KEY(periodo_id) REFERENCES periodo(id))')
    con.commit()
    con.close()
