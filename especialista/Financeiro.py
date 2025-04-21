from .AbstractEspecialista import AbstractEspecialista

class Financeiro(AbstractEspecialista):
     
    def pode_responder(self, tarefa):
        return "preço" in tarefa or "faturamento" in tarefa or "pagamento" in tarefa

    def responder(self, tarefa):
        return "Preço sugerido baseado na análise de mercado. Faturamento atualizado."