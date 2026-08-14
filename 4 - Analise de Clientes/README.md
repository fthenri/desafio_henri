1
Conectei as chaves da seguinte forma: 
orders (id) -> order_items (order_id) -> product_variants (id através de product_variant_id) -> products (id através de product_id) -> categories (id através de category_id). Depois, eu agrupei pelo ID e nome da categoria e somei os itens comprados com SUM(quantity)

2
Concentrei o cálculo em uma CTE nomeada diversidade, onde utilizei COUNT(DISTINCT p.category_id) e fiz o agrupamento por customer_id. No grupo de validação, utilizei o filtro WHERE diversidade_categorias >= 13

3
Isolei os 10 clientes top em uma CTE dedicada (top_10_clientes) e ordenei eles pelo ticket médio decrescente com LIMIT 10. No último SELECT, eu usei a cláusula WHERE para filtrar e garantir que só as transações dos clientes selecionados fossem consideradas, ou seja, apenas aquelas onde o.customer_id está presente na subconsulta (SELECT customer_id FROM top_10_clientes) que identifica os top 10 clientes