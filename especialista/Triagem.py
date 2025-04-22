import random
from .AbstractEspecialista import AbstractEspecialista

class Triagem(AbstractEspecialista):
    def __init__(self, gerador):
        self.sintomas = []
        self.gerador = gerador

    def eh_ativado(self):
        return bool(self.Bancada.estadoCompartilhado['sintomas'])
    
    @property
    def expertise(self):
        return "triagem"

    @property
    def progresso(self):
        return random.randint(20, 50)

    def contribui(self):
        sintomas = self.Bancada.estadoCompartilhado['sintomas']

        if not sintomas:
            return

        print("Triagem está analisando os sintomas e incluíndo atividade na bancada")

        if 'computador_com_problema' in sintomas:
        # Lista todos os métodos disponíveis de tarefas
            opcoes = [
                self.gerador.funcionamento_normal,
                self.gerador.conectar_alimentacao,
                self.gerador.fonte_queimada,
                self.gerador.circuito_de_alimentacao,
                self.gerador.fonte_com_problema,
                self.gerador.checar_processador_e_memoria_ram,
                self.gerador.problema_na_placa_mae,
                self.gerador.hd_ou_ssd_desconectado_ou_com_defeito,
                self.gerador.ajustar_boot,
                self.gerador.substituir_hd_ou_ssd,
                self.gerador.imagem_so_corrompida
            ]
    
            tarefa_func = random.choice(opcoes)
            descricao, problema = tarefa_func()  # obtém retorno do método
            self.Bancada.estadoCompartilhado['problemas'].append(problema)
            self.Bancada.adicionaTarefa(problema, [descricao])
    
            self.Bancada.adicionaContribuicao(['Triagem', [problema]])
            self.Bancada.estadoCompartilhado['sintomas'] = []