import pandas as pd
import os
from src.task import Task

class Transformar(Task):
    def __init__(self):
        super().__init__("Transformar")
        self.data_dir = os.path.join(os.path.dirname(os.path.dirname(os.path.dirname(__file__))), 'data')
        
    def run(self):
        input_file = os.path.join(self.data_dir, 'input.csv')
        df = pd.read_csv(input_file)
        df['data_nascimento'] = pd.to_datetime(df['data_nascimento'])
        df['data_pedido'] = pd.to_datetime(df['data_pedido'])
        df['idade'] = ((pd.Timestamp.now() - df['data_nascimento']).dt.days / 365).round(0)
        df['mes_pedido'] = df['data_pedido'].dt.month
        df['trimestre_pedido'] = df['data_pedido'].dt.quarter
        df['ano_pedido'] = df['data_pedido'].dt.year
        df_agg = df.groupby(['categoria_produto', 'status_pedido']).agg({
            'valor_compra': ['sum', 'mean', 'count'],
            'idade': 'mean'
        }).reset_index()

        df_agg.columns = ['categoria_produto', 'status_pedido', 
                         'valor_total', 'valor_medio', 'quantidade_pedidos', 
                         'idade_media']
        
        total_valor = df_agg['valor_total'].sum()
        df_agg['percentual_valor'] = (df_agg['valor_total'] / total_valor * 100).round(2)
        
        stage_file = os.path.join(self.data_dir, 'stage.csv')
        df_agg.to_csv(stage_file, index=False) 
