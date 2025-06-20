import pandas as pd
import os
from src.task import Task

class Carregar(Task):
    def __init__(self):
        super().__init__("Carregar")
        self.data_dir = os.path.join(os.path.dirname(os.path.dirname(os.path.dirname(__file__))), 'data')
        
    def run(self):
        stage_file = os.path.join(self.data_dir, 'stage.csv')
        df = pd.read_csv(stage_file)
        
        df['status_prioritario'] = df['status_pedido'].apply(
            lambda x: 'Sim' if x in ['Em Processamento', 'Entregue'] else 'Não'
        )
        
        df['valor_por_pedido'] = (df['valor_total'] / df['quantidade_pedidos']).round(2)
        
        df['data_processamento'] = pd.Timestamp.now().strftime('%Y-%m-%d %H:%M:%S')
        
        df = df.sort_values('valor_total', ascending=False)
        
        output_file = os.path.join(self.data_dir, 'output.csv')
        df.to_csv(output_file, index=False) 
