

# Controla o acesso de cada especialista ao quadro-negro para pegar uma tarefa da
# lista 'instancias-de-problemas', chama cada especialista a contribuir e
# adiciona o resultado/contribuição na lista de contribuições do quadro-negro.
class Controlador:
    def __init__(self, especialistas):
        self.especialistas = especialistas

    def distribuir_tarefas(self, quadro_negro):
        print("\n Controlador: Distribuindo tarefas para os especialistas...")

        for tarefa in quadro_negro.tarefas:
            if tarefa.status == "pendente":
                print(f"\n Tarefa {tarefa.id}: {tarefa.descricao}")

                for esp in self.especialistas:
                    if esp.pode_responder(tarefa.descricao.lower()):
                        resposta = esp.responder(tarefa.descricao)
                        print(f"   {esp.__class__.__name__} contribuiu: {resposta}")
                        quadro_negro.adicionar_contribuicao(tarefa.id, esp.__class__.__name__, resposta)

                # Aqui, se quiser, você pode marcar a tarefa como "em andamento" ou deixar como "pendente"
                tarefa.status = "em andamento"
