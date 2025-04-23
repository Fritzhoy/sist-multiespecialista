import random
from .AbstractEspecialista import AbstractEspecialista

class Eletricista(AbstractEspecialista):
    def eh_ativado(self):
        if'falha_eletrica' in self.Bancada.estadoCompartilhado['problemas']:
            return True
        else:
            return False
    @property
    def expertise(self):
        p = None
        if 'falha_eletrica' in self.Bancada.estadoCompartilhado['problemas']:
            p = self.Bancada.pegaParametros('falha_eletrica')
            return ['falha_eletrica', p]

    @property
    def progresso(self):
        return random.randint(20, 120)

    def contribui(self):
        self.Bancada.adicionaContribuicao([[self.__class__.__name__, self.expertise]])
        self.Bancada.atualizaProgresso(self.progresso)
        

        # Adiciona próxima tarefa para Finalizador
        self.Bancada.estadoCompartilhado['problemas'].append('verificacao_final')
        self.Bancada.adicionaTarefa('verificacao_final', ['computador pronto para teste final'])
