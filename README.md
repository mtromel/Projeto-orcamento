# Projeto de sistema de orçamento pessoal

Este projeto tem o objetivo de criar um sistema de controle de orçamento
baseado no método apresentado pela especialista em finanças, apresentadora e
jornalista Nath Arcuri no seu livro *Me Poupe* onde ela sugere fazer um
planejamento e controle de orçamento usando os seguintes parâmetros:

Categoria     | % das receitas
------------- | :------------:
Essenciais    | 55%
Educação      | 5%
Objetivos     | 20%
Aposentadoria | 10%
Gastar        | 10%

Para isso o sistema permite vincular uma despesa registrada a um desses grupos
de planejamento. Nesta primeira versão do sistema é possível acompanhar o
andamento do planejamento por meio de relatórios. Melhorias futuras vão
permitir que existam alertas e gráficos mostrando o planejamento do mês atual
e de meses futuros também.

Além disso o sistema permite o cadastramento de categorias de despesas que
são usadas em relatórios onde as despesas são agrupadas e somadas por categoria
permitindo uma visualização fácil e rápida de como as despesas estão sendo 
realizadas em um período.

Chamei de período ao invés de mês porque acho mais interessante separar pela
data de pagamento de uma despesa, ao invés de pela data de realização da
despesa. Esse conceito fica fácil de entender ao olhar para uma fatura de
cartão de crédito, por exemplo. Digamos que o vencimento da fatura seja no dia
10 de cada mês, mas as despesas que ela engloba normalmente vão abranger do dia
5 do mês anterior até o dia 4 do mês atual. Mas como ela só é paga no mês atual
acho mais interessante considerar que ela faz parte do período do mês atual já
que o valor para o pagamento dessa fatura sairá das receitas do mês atual.

Achei produtivo também permitir o cadastramento de despesas recorrentes, que
chamei de fixas, tais como Luz, Internet, Condomínio, Aluguel. Assim ao iniciar
os lançamentos para um novo período, não será necessário que o usuário digite
novamente todas essas despesas que normalmente tem o mesmo valor e data de
pagamento. Mas se houver alguma alteração de valor ou data de pagamento é
possível fazer o ajuste apenas no mês atual, ou então, se for uma mudança
definitiva, pode ser alterada na tabela de despesas fixas. Ao iniciar os
lançamentos de despesas para um novo período o sistema vai reconhecer que não
existem lançamentos para esse período e vai sugerir copiar todas as despesas
fixas cadastradas, evitando assim a redigitação.

O mesmo acontece com as receitas.

### Histórico de Versões:

###### Versão 1.0

Nesta versão procurei usar apenas os conceitos de python e criei um sistema
para ser usado por terminal e linha de comando. Os relatórios são básicos e
com visual muito simples.
