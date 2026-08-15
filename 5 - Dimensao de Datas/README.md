5.1 - script.sql

5.2 -

1. Pois a tabela de vendas só armazena transações.  Um dia em que não há vendas nas lojas físicas significa que não há nenhuma linha no banco de dados para essa data.  Quando se agrupa diretamente pela tabela orders, o banco de dados calcula a média sem contar os dias sem vendas, ou seja, desconsiderando matematicamente esses dias, resultando em um denominador menor do que o real e, consequentemente, aumentando a média final. O calendário impõe a presença da linha no entroncamento

2. Se não utilizássemos o calendário, a média desse dia da semana continuaria elevada de forma artificial, uma vez que o sistema calcularia essa média apenas com base nos dias de pico em que a loja abriu e teve um volume alto de vendas. Com a adição da dimensão de datas e do LEFT JOIN com COALESCE, os dias que estão fechados ou com zero são contabilizados como valor 0, o que eleva o denominador da fórmula da média e expõe a verdadeira performance, ou prejuizo, que está espalhada ao longo de todos os meses