-- database: ecommerce.db
SELECT * FROM vendas;

SELECT strftime('%Y', data_pagamento) AS ano, COUNT(*) AS total_vendas
FROM vendas
GROUP BY ano;

SELECT * FROM vendas WHERE status_entrega = 'Entregue';

