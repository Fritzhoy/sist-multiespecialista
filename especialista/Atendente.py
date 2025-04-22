import random
from .AbstractEspecialista import AbstractEspecialista
from .Triagem import Triagem

class Atendente(AbstractEspecialista):

    def eh_ativado(self):
        return 'computador_com_problema' in self.Bancada.estadoCompartilhado['problemas']

    @property
    def expertise(self):
        p = self.Bancada.pegaTarefa('computador_com_problema')
        return ['computador_com_problema', p]

    @property
    def progresso(self):
        return random.randint(10, 20)

    def contribui(self):
        sintomas_iniciais = ['computador_com_problema']
        
        # Registra a contribuição
        self.Bancada.adicionaContribuicao([[self.__class__.__name__, sintomas_iniciais]])
        self.Bancada.atualizaProgresso(self.progresso)

        # Envia para triagem
        self.Bancada.estadoCompartilhado['sintomas'] = sintomas_iniciais
        print("Atendente recebeu o computador e encaminhou para a triagem.")

        # # Remove o problema tratado para não entrar em loop
        # if 'computador_com_problema' in self.Bancada.estadoCompartilhado['problemas']:
        #     self.Bancada.estadoCompartilhado['problemas'].remove('computador_com_problema')