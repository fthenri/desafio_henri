# 1.1 = script sql

# 1.2 = 28704.992077227642

# 1.3 - Interpretação
> A tabela indica que não está pronta para análises e exige tratamento prévio. 

> Pontos de atenção identificados:

## Outliers em 'total'
- min = 32,62
- max = 127.262,02
- media = 28.704,99

O que indica grandes outliers ou mistura de categorias muito distintas (Pequenas peças x Venda de uma lancha) o que acaba por distorcer a média ou o modelo preditivo.

## Inconsistencia nas datas
A data maxima é 2026-12-31, o que indica dados no futuro ou dados simulados.
Isso pode gerar data leakage em análises preditivas se não for filtrado.

## Orders precisa de outro relacionamento
A coluna 'orders' deve ser obrigatoriamente cruzada com order_items, products e customers.
Isso para que saibamos o que foi vendido e para quem.





