from .AbstractEspecialista import AbstractEspecialista

# Aluno 'é-um' AbstractEspecialista
class Editorial(AbstractEspecialista):
    
    def pode_responder(self, tarefa):
        return "texto" in tarefa or "revisar" in tarefa or "gramática" in tarefa

    def responder(self, tarefa):
        return "Texto revisado com sucesso. Sugestões de melhoria enviadas ao autor."

