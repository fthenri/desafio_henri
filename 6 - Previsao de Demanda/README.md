6.1 - previsao.ipynb

6.2 - 149

6.3

1 - O baseline foi construido usando media movel trimestral. 
O dataset foi concentrado no produto mais vendido 'Bússola de Bordo 702',
garanti que estavaos analizando com base na data do pedido (created_at_order),
agrupei tudo mês a mês e os meses sem vendas eu coloquei valor zero de vez de nulo.
O modelo ficou simples: a previsão é sempre a media dos 3 meses anteriores ao mês da previsão

2 - Apliquei o shift(1) do pandas no calculo da janela movel. Ou seja, os resultados obtidos,
da media trimestral são empurrados um mês a frente de vez de corresponderem ao último mês do trimestre.
Isso isola os meses que usamos para o calculo, por exemplo:
Queremos prever abril, então o calculo pega Janeiro, Fevereiro e Março e joga o resultado no mês de abril.
Assim nunca há exposição do resultado real no calculo.

3 - O maior problema de usar media movel assim é a reatividade e livre de contexto. Por exemplo, 
o modelo atual não entende a possibilidade de produtos serem mais vendidos durante o verão.
Como ele usa o mesmo peso em todos os meses ele não consegue compreender nem prever um pico de vendas.
Ele gera uma curva suave que chega atrasado na tendencia do mercado.