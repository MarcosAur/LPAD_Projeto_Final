import pandas as pd
import numpy as np
import os
from faker import Faker
from src.task import Task

class Extrair(Task):
    def __init__(self):
        super().__init__("Extrair")
        self.data_dir = os.path.join(os.path.dirname(os.path.dirname(os.path.dirname(__file__))), 'data')
        self.fake = Faker('pt_BR')  
        
    def run(self):
        np.random.seed(42)
        n_rows = 12000

        data = {
            'id': range(1, n_rows + 1),
            'nome': [self.fake.name() for _ in range(n_rows)],
            'email': [self.fake.email() for _ in range(n_rows)],
            'telefone': [self.fake.phone_number() for _ in range(n_rows)],
            'endereco': [self.fake.address() for _ in range(n_rows)],
            'cidade': [self.fake.city() for _ in range(n_rows)],
            'estado': [self.fake.state_abbr() for _ in range(n_rows)],
            'data_nascimento': [self.fake.date_of_birth(minimum_age=18, maximum_age=80) for _ in range(n_rows)],
            'valor_compra': np.random.uniform(50, 2000, n_rows).round(2),
            'categoria_produto': np.random.choice(['Eletrônicos', 'Vestuário', 'Alimentos', 'Móveis', 'Livros'], n_rows),
            'forma_pagamento': np.random.choice(['Cartão de Crédito', 'Boleto', 'PIX', 'Transferência'], n_rows),
            'status_pedido': np.random.choice(['Concluído', 'Em Processamento', 'Cancelado', 'Entregue'], n_rows),
            'data_pedido': [self.fake.date_time_between(start_date='-1y', end_date='now') for _ in range(n_rows)]
        }
        df = pd.DataFrame(data)

        input_file = os.path.join(self.data_dir, 'input.csv')
        df.to_csv(input_file, index=False) 
