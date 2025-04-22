import random
from .AbstractEspecialista import AbstractEspecialista

class Testador(AbstractEspecialista):

    def eh_ativado(self):
        return 'verificacao_final' in self.Bancada.estadoCompartilhado['problemas']

    @property
    def expertise(self):
        p = self.Bancada.pegaParametros('verificacao_final')
        return ['verificacao_final', p]

    @property
    def progresso(self):
        return random.randint(10, 30)

    def contribui(self):

        self.Bancada.adicionaContribuicao([[self.__class__.__name__, self.expertise]])
        self.Bancada.atualizaProgresso(self.progresso)

        # Finaliza o processo com sucesso
        self.Bancada.estadoCompartilhado['problemas'].remove('verificacao_final')
        self.Bancada.adicionaTarefa('funcionamento_normal', ['computador ligando e operacional'])
