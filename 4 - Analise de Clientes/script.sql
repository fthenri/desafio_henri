-- tarefa 1 e 2

WITH fat_freq AS (
    SELECT 
        customer_id,
        SUM(total) AS faturamento_total,
        COUNT(id) AS frequencia,
        SUM(total) / COUNT(id) AS ticket_medio
    FROM orders
    GROUP BY customer_id
),
diversidade AS (
    SELECT 
        o.customer_id,
        COUNT(DISTINCT p.category_id) AS diversidade_categorias
    FROM orders o
    JOIN order_items oi ON o.id = oi.order_id
    JOIN product_variants pv ON oi.product_variant_id = pv.id
    JOIN products p ON pv.product_id = p.id
    GROUP BY o.customer_id
)
SELECT 
    f.customer_id,
    f.faturamento_total,
    f.frequencia,
    f.ticket_medio,
    d.diversidade_categorias
FROM fat_freq f
JOIN diversidade d ON f.customer_id = d.customer_id
WHERE d.diversidade_categorias >= 13
ORDER BY f.ticket_medio DESC, f.customer_id ASC
LIMIT 10;

-- tarefa 3

WITH fat_freq AS (
    SELECT 
        customer_id,
        SUM(total) / COUNT(id) AS ticket_medio
    FROM orders
    GROUP BY customer_id
),
diversidade AS (
    SELECT 
        o.customer_id,
        COUNT(DISTINCT p.category_id) AS diversidade_categorias
    FROM orders o
    JOIN order_items oi ON o.id = oi.order_id
    JOIN product_variants pv ON oi.product_variant_id = pv.id
    JOIN products p ON pv.product_id = p.id
    GROUP BY o.customer_id
),
top_10_clientes AS (
    SELECT f.customer_id
    FROM fat_freq f
    JOIN diversidade d ON f.customer_id = d.customer_id
    WHERE d.diversidade_categorias >= 13
    ORDER BY f.ticket_medio DESC, f.customer_id ASC
    LIMIT 10
)
SELECT 
    p.category_id,
    c.name AS category_name,
    SUM(oi.quantity) AS total_itens_comprados
FROM orders o
JOIN order_items oi ON o.id = oi.order_id
JOIN product_variants pv ON oi.product_variant_id = pv.id
JOIN products p ON pv.product_id = p.id
JOIN categories c ON p.category_id = c.id
WHERE o.customer_id IN (SELECT customer_id FROM top_10_clientes)
GROUP BY p.category_id, c.name
ORDER BY total_itens_comprados DESC
LIMIT 1;