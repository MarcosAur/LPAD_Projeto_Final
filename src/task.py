from abc import ABC, abstractmethod
import time
from datetime import datetime
from .utils.logger import Logger

class Task(ABC):
    def __init__(self, name):
        self.name = name
        self.logger = Logger()
        
    def execute(self):
        start_time = time.time()
        try:
            print(f"Executando tarefa: {self.name}")
            self.run()
            execution_time = time.time() - start_time
            self.logger.info(f"{self.name} - OK - {execution_time:.2f}s")
            print(f"Tarefa {self.name} finalizada com sucesso.\n")
        except Exception as e:
            execution_time = time.time() - start_time
            self.logger.error(f"{self.name} - ERRO: {str(e)} - {execution_time:.2f}s")
            raise
    
    @abstractmethod
    def run(self):
        """Método que deve ser implementado pelas classes filhas"""
        pass 
