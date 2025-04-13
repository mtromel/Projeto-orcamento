import sys
from pathlib import Path

import utils

THIS_FOLDER = Path(__file__).parent.resolve()

con, cur = utils.conectar_bd(THIS_FOLDER / 'bd_orcamento.db')

if con:
    print('Conexão com o bd ok!')
else:
    print('Erro na conexão com o bd!')

print(*sys.path, sep='\n')

consulta = cur.execute('SELECT d.desc_loja, d.desc_desp, d.data, d.valor,'
                       ' c.categoria, d.parcela_atual, d.parcelas_total,'
                       ' p.grupo, d.tipo, o.origem, per.periodo FROM despesas'
                       ' AS d INNER JOIN categorias AS c ON'
                       ' d.categoria_id=c.id INNER JOIN planejamento AS p ON'
                       ' d.grupo_id=p.id INNER JOIN origem AS o ON'
                       ' d.origem_id=o.id INNER JOIN periodo AS per ON'
                       ' d.periodo_id=per.id')

print(*consulta.fetchall(), sep='\n')
