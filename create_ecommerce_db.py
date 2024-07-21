import sqlite3
from faker import Faker
import random
from datetime import datetime

# Criação do banco de dados SQLite e conexão
conn = sqlite3.connect('ecommerce.db')
cursor = conn.cursor()

# Criação da tabela
cursor.execute('''
    CREATE TABLE IF NOT EXISTS vendas (
        id INTEGER PRIMARY KEY,
        cliente TEXT,
        valor_pago REAL,
        produto TEXT,
        data_pagamento TEXT,
        status_entrega TEXT
    )
''')

# Inicialização do Faker para gerar dados aleatórios
fake = Faker('pt_BR')
Faker.seed(0)
random.seed(0)

# Listas para gerar dados aleatórios
produtos = ['Brinquedo', 'Ferramenta', 'Utensílio Doméstico']
status = ['Entregue', 'Em Devolução', 'Cancelado', 'Extraviado', 'Devolvido']

# Função para gerar datas aleatórias entre 2019 e 2024
def random_date(start, end):
    return fake.date_between(start_date=start, end_date=end)

# Inserção de 1000 linhas na tabela
for _ in range(1000):
    cliente = fake.name()
    valor_pago = round(random.uniform(100, 5000), 2)
    produto = random.choice(produtos)
    data_pagamento = random_date(datetime(2019, 1, 1), datetime(2024, 12, 31)).isoformat()
    status_entrega = random.choice(status)
    
    cursor.execute('''
        INSERT INTO vendas (cliente, valor_pago, produto, data_pagamento, status_entrega)
        VALUES (?, ?, ?, ?, ?)
    ''', (cliente, valor_pago, produto, data_pagamento, status_entrega))

# Salvando as alterações e fechando a conexão
conn.commit()
conn.close()
