class Bancada:
    def __init__(self):
        self.estadoCompartilhado = {
            'sintomas': [],
            'problemas': ['computador_com_problema'],
            'instancias': {'computador_com_problema': [],
                        },
            'contribuicoes': [],
            'progresso': 0
        }
        self.especialistas = []

    def adicionaEspecialista(self, esp):
        self.especialistas.append(esp)

    def adicionaSintomas(self, sintomas):
        self.estadoCompartilhado['sintomas'] += sintomas

    def adicionaTarefa(self, problema, parametros):
        self.estadoCompartilhado['problemas'].append(problema)
        self.estadoCompartilhado['instancias'][problema] = parametros

    def pegaParametros(self, problema):
        return self.estadoCompartilhado['instancias'].get(problema, [])
    
    def mostraTarefas(self):
        print('instancias',self.estadoCompartilhado['instancias'])

    def adicionaContribuicao(self, contrib):
        self.estadoCompartilhado['contribuicoes'].append(contrib)

    def atualizaProgresso(self, valor):
        self.estadoCompartilhado['progresso'] += valor