-- Selecionar todos os dados da tabela vendas
SELECT * FROM vendas;


-- Selecionar clientes que pagaram mais de 1000 reais
SELECT * FROM vendas WHERE valor_pago > 1000;

-- Selecionar vendas de um produto específico
SELECT * FROM vendas WHERE produto = 'Brinquedo';

-- Selecionar vendas por ano
SELECT strftime('%Y', data_pagamento) AS ano, COUNT(*) AS total_vendas
FROM vendas
GROUP BY ano;

-- Selecionar vendas com status de entrega específico
SELECT * FROM vendas WHERE status_entrega = 'Entregue';
