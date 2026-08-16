WITH parametros_datas AS (
    SELECT 
        MIN(DATE(created_at)) AS data_inicio,
        MAX(DATE(created_at)) AS data_fim
    FROM orders
    WHERE channel = 'pos'
),
calendario AS (
    SELECT generate_series(
        (SELECT data_inicio FROM parametros_datas),
        (SELECT data_fim FROM parametros_datas),
        '1 day'::interval
    )::date AS data_calendario
),
vendas_diarias_pos AS (
    SELECT 
        DATE(created_at) AS data_venda,
        SUM(total) AS soma_vendas
    FROM orders
    WHERE channel = 'pos'
    GROUP BY DATE(created_at)
)
SELECT 
    CASE EXTRACT(DOW FROM c.data_calendario)
        WHEN 0 THEN 'Domingo'
        WHEN 1 THEN 'Segunda-feira'
        WHEN 2 THEN 'Terça-feira'
        WHEN 3 THEN 'Quarta-feira'
        WHEN 4 THEN 'Quinta-feira'
        WHEN 5 THEN 'Sexta-feira'
        WHEN 6 THEN 'Sábado'
    END AS dia_semana,
    AVG(COALESCE(v.soma_vendas, 0)) AS media_vendas
FROM calendario c
LEFT JOIN vendas_diarias_pos v ON c.data_calendario = v.data_venda
GROUP BY EXTRACT(DOW FROM c.data_calendario), dia_semana
ORDER BY media_vendas ASC;