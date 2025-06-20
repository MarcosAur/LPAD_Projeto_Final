from abc import ABC, abstractmethod
import time
from datetime import datetime
from .utils.logger import log_execution

class Task(ABC):
    def __init__(self, name):
        self.name = name
        
    def execute(self):
        start_time = time.time()
        try:
            print(f"Executando tarefa: {self.name}")
            self.run()
            execution_time = time.time() - start_time
            log_execution(self.name, "OK", execution_time)
            print(f"Tarefa {self.name} finalizada com sucesso.\n")
        except Exception as e:
            execution_time = time.time() - start_time
            log_execution(self.name, f"ERRO: {str(e)}", execution_time)
            raise
    
    @abstractmethod
    def run(self):
        """Método que deve ser implementado pelas classes filhas"""
        pass 
