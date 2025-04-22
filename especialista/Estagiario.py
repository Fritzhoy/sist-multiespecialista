import random
from .AbstractEspecialista import AbstractEspecialista

class Estagiario(AbstractEspecialista):
    def eh_ativado(self):
        return 'msg_erro_boot' in self.Bancada.estadoCompartilhado['problemas']

    @property
    def expertise(self):
        p = None
        if 'msg_erro_boot' in self.Bancada.estadoCompartilhado['problemas']:
            p = self.Bancada.pegaParametros('msg_erro_boot')
            return ['msg_erro_boot', p]

    @property
    def progresso(self):
        return random.randint(20, 120)

    def contribui(self):
        self.Bancada.adicionaContribuicao([[self.__class__.__name__, self.expertise]])
        self.Bancada.atualizaProgresso(self.progresso)
    
        # Adiciona próxima tarefa para Finalizador
        self.Bancada.estadoCompartilhado['problemas'].append('verificacao_final')
        self.Bancada.adicionaTarefa('verificacao_final', ['computador pronto para teste final'])
