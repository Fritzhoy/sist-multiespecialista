import random
from .AbstractEspecialista import AbstractEspecialista

class Tecnico(AbstractEspecialista):
    def eh_ativado(self):
        if 'problema_software' in self.Bancada.estadoCompartilhado['problemas']:
            return True
        else: 
            return False
        
    @property
    def expertise(self):
        p = None
        if 'problema_software' in self.Bancada.estadoCompartilhado['problemas']:
            p = self.Bancada.pegaParametros('problema_software')
            return ['problema_software', p]

    @property
    def progresso(self):
        return random.randint(20, 120)

    def contribui(self):
        self.Bancada.adicionaContribuicao([[self.__class__.__name__, self.expertise]])
        self.Bancada.atualizaProgresso(self.progresso)
        
        # Adiciona próxima tarefa para Finalizador
        self.Bancada.estadoCompartilhado['problemas'].append('verificacao_final')
        self.Bancada.adicionaTarefa('verificacao_final', ['computador pronto para teste final'])