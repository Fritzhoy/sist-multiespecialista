from .AbstractEspecialista import AbstractEspecialista

class Marketing(AbstractEspecialista):
    def pode_responder(self, tarefa):
        return "divulgação" in tarefa or "sinopse" in tarefa or "campanha" in tarefa

    def responder(self, tarefa):
        return "Campanha de marketing criada com foco no público-alvo ideal."