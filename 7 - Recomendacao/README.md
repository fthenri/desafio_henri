7.1 - recomendacao.ipynb

7.2 - Motor de Popa 5331

7.3 - 

1 - A matriz foi construida cruzando itens, pedidos e variantes,
relacionando diretamente costumer_id com product_id.
Depois aplicamos um drop_duplicates() para focar na presença ou ausencia.
Por fim usei pivot do pandas para fazer uma matriz gigante, linha cliente, coluna produto,
1 = comprou
0 = não comprou

2 - O cosseno compara o público de dois itens, se a lista de usuarios que comprou o produto A
for quase identica a lista de quem comprou o produto B o resultado se aproxima de 1.
Já se não cruza nenhum produto entre as listas então o resultado é 0.
É basicamente uma forma matematica e dizer que se o seu carrinho tem isso você gostará daquilo.

3 - O problema desse método é chamado de cold start, onde, como a tradução do nome ja diz,
o produto sofre de falta de dados ao ser adicionado pela loja ja que precisa de dados 
sendo cruzados para que seja recomendado um produto. 
Se amanhã colocarmos um produto novo na loja levará um tempo e volume para que comece a
ser recomendado o produto que adicionamos aos clientes

