class AbstractEspecialista:
    def pode_responder(self, tarefa: str) -> bool:
        raise NotImplementedError

    def responder(self, tarefa: str) -> str:
        raise NotImplementedError
