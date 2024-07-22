# Banco de Dados: ecommerce.db

Este repositório contém o banco de dados de um ecommerce fictício, desenvolvido como parte de um estudo de caso para análise de dados e SQL.

## Funcionalidades Implementadas

- **Consultas de Dados Gerais**: Selecionar todos os dados da tabela `vendas`.
- **Consultas Específicas**:
  - Selecionar clientes que pagaram mais de 1000 reais.
  - Selecionar vendas de um produto específico.
  - Selecionar vendas por ano.
  - Selecionar vendas com status de entrega específico.
  - Selecionar vendas com produtos iguais a ferramenta.

Problemas Corrigidos
Consultas Otimizadas: Melhoramos a eficiência das consultas para grandes volumes de dados.
Correção de Dados: Corrigido o tratamento de datas e valores inconsistentes nas consultas.
Estrutura do Banco de Dados
ecommerce.db
Contém o banco de dados SQLite com a tabela vendas, incluindo colunas como id, cliente_id, produto, valor_pago, data_pagamento, e status_entrega.
Como Usar
Clone o repositório.
Abra o banco de dados em um visualizador de SQLite ou uma ferramenta de gerenciamento de bancos de dados.
Execute as consultas SQL fornecidas para analisar os dados de vendas.
