import random

class GeradorDeTarefa(object):

    def __init__(self, bancada):
        self.Bancada = bancada

    def funcionamento_normal(self):
        return ['Verificou que o computador está funcionando perfeitamente!', 'sem_erros']

    def conectar_alimentacao(self):
        return ['Ligou o computador na tomada!', 'falha_eletrica']

    def fonte_queimada(self):
        return ['Trocou a fonte de energia porque estava queimada!', 'falha_eletrica']

    def circuito_de_alimentacao(self):
        return ['Diagnosticou que o circuito de alimentação da placa mãe estava estava com problema!', 'falha_eletrica']
    
    def fonte_com_problema(self):
        return ['Encaminhou a fonte de energia para a assistência porque estava com problema!', 'falha_eletrica']

    def checar_processador_e_memoria_ram(self):
        return ['Trocou a pasta térmica e passou borracha na memória ram e resolveu!', 'problema_hardware']
    
    def problema_na_placa_mae(self):
        return ['Trocou a placa mãe porque estava com problema!', 'problema_hardware']
    
    def hd_ou_ssd_desconectado_ou_com_defeito(self):
        return ['Conectou o cabo do HD que estava mal conectado!', 'problema_hardware']
    
    def ajustar_boot(self):
        return ['Ajustou o boot do computador para inicializar pelo HD!', 'problema_software']
    
    def substituir_hd_ou_ssd(self):
        return ['Substituiu o HD por um novo!', 'problema_hardware']
    
    def imagem_so_corrompida(self):
        return ['Reinstalou o sistema operacional porque a imagem estava corrompida!', 'problema_software']
    
   
    def adicionaTarefa(self):
        self.Bancada.adicionaTarefa('funcionamento_normal', self.funcionamento_normal())
        self.Bancada.adicionaTarefa('conectar_alimentacao', self.conectar_alimentacao())
        self.Bancada.adicionaTarefa('fonte_queimada', self.fonte_queimada())
        self.Bancada.adicionaTarefa('circuito_de_alimentacao', self.circuito_de_alimentacao())
        self.Bancada.adicionaTarefa('fonte_com_problema', self.fonte_com_problema())
        self.Bancada.adicionaTarefa('checar_processador_e_memoria_ram', self.checar_processador_e_memoria_ram())
        self.Bancada.adicionaTarefa('problema_na_placa_mae', self.problema_na_placa_mae())
        self.Bancada.adicionaTarefa('hd_ou_ssd_desconectado_ou_com_defeito', self.hd_ou_ssd_desconectado_ou_com_defeito())
        self.Bancada.adicionaTarefa('ajustar_boot', self.ajustar_boot())
        self.Bancada.adicionaTarefa('substituir_hd_ou_ssd', self.substituir_hd_ou_ssd())
        self.Bancada.adicionaTarefa('imagem_so_corrompida', self.imagem_so_corrompida())