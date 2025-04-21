from .AbstractEspecialista import AbstractEspecialista

class Logistica(AbstractEspecialista):
    def pode_responder(self, tarefa):
        return "entrega" in tarefa or "estoque" in tarefa or "distribuição" in tarefa

    def responder(self, tarefa):
        return "Distribuição agendada e estoques atualizados."
