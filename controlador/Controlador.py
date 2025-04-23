

# Controla o acesso de cada especialista ao quadro-negro para pegar uma tarefa da
# lista 'instancias-de-problemas', chama cada especialista a contribuir e
# adiciona o resultado/contribuição na lista de contribuições do quadro-negro.
class Controlador:
    
    def __init__(self, bancada, GeradorDeTarefa, limite = 120):
        self.Bancada = bancada
        self.GeradorDeTarefa = GeradorDeTarefa
        self.limite = limite

    def loop(self):
      while self.Bancada.estadoCompartilhado['progresso'] < self.limite:
          self.GeradorDeTarefa.adicionaTarefa()
          #self.Bancada.mostraTarefas()
          for especialista in self.Bancada.especialistas:
              if especialista.eh_ativado:
                  especialista.contribui()
      return self.Bancada.estadoCompartilhado['contribuicoes']