import os
import sys

sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from src.pipeline import Pipeline
from src.tasks.extrair import Extrair
from src.tasks.transformar import Transformar
from src.tasks.carregar import Carregar

def main():
    pipeline = Pipeline()
    pipeline.add_task(Extrair())
    pipeline.add_task(Transformar())
    pipeline.add_task(Carregar())
    pipeline.execute()

if __name__ == "__main__":
    main() 
