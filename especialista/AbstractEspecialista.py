from abc import ABC, abstractmethod

class AbstractEspecialista(ABC):
    def __init__(self):
        self.Bancada = None

    @abstractmethod
    def eh_ativado(self): pass

    @abstractmethod
    def contribui(self): pass