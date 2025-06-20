class Pipeline:
    def __init__(self):
        self.tasks = []
    
    def add_task(self, task):
        """Adiciona uma tarefa à pipeline"""
        self.tasks.append(task)
    
    def execute(self):
        """Executa todas as tarefas na ordem em que foram adicionadas"""
        for task in self.tasks:
            task.execute() 
