import random
from .AbstractEspecialista import AbstractEspecialista

class Finalizador(AbstractEspecialista):

    def eh_ativado(self):
        return 'funcionamento_normal' in self.Bancada.estadoCompartilhado['problemas']

    @property
    def expertise(self):
        p = self.Bancada.pegaParametros('funcionamento_normal')
        return ['funcionamento_normal', p]

    @property
    def progresso(self):
        return random.randint(10, 30)

    def contribui(self):
        self.Bancada.adicionaContribuicao([[self.__class__.__name__, self.expertise]])
        self.Bancada.atualizaProgresso(self.progresso)

