import random
from .AbstractEspecialista import AbstractEspecialista

class EngEletrico(AbstractEspecialista):
     
    def eh_ativado(self):
        return 'problema_hardware' in self.Bancada.estadoCompartilhado['problemas']

    @property
    def expertise(self):
        p = None
        if 'problema_hardware' in self.Bancada.estadoCompartilhado['problemas']:
            p = self.Bancada.pegaParametros('problema_hardware')  
            return ['problema_hardware', p]

    @property
    def progresso(self):
        return random.randint(20, 120)

    def contribui(self):

        self.Bancada.adicionaContribuicao([[self.__class__.__name__, self.expertise]])
        self.Bancada.atualizaProgresso(self.progresso)

        # Adiciona próxima tarefa para Finalizador
        self.Bancada.estadoCompartilhado['problemas'].append('verificacao_final')
        self.Bancada.adicionaTarefa('verificacao_final', ['computador pronto para teste final'])
    
