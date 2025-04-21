from especialista.Editorial import Editorial
from especialista.Marketing import Marketing
from especialista.Logistica import Logistica
from especialista.Financeiro import Financeiro
from blackboard.QuadroNegro import QuadroNegro
from geradordetarefa.GeradorDeTarefa import GeradorDeTarefa
from controlador import Controlador

class SistemaEditora:

    def __init__(self):
        self.especialistas = [
            Editorial(),
            Marketing(),
            Logistica(),
            Financeiro()
        ]

    def processar_tarefa(self, tarefa: str) -> str:
        for esp in self.especialistas:
            if esp.pode_responder(tarefa.lower()):
                return esp.responder(tarefa)
        return "Nenhum especialista disponível para essa tarefa."
    
    def processar_tarefa_com_autor(self, tarefa: str) -> tuple[str, str]:
        for esp in self.especialistas:
            if esp.pode_responder(tarefa.lower()):
                return esp.responder(tarefa), esp.__class__.__name__
        return "Nenhum especialista disponível para essa tarefa.", "Desconhecido"

# Execução
if __name__ == "__main__":
    sistema = SistemaEditora()
    quadro = QuadroNegro()
    gerador = GeradorDeTarefa()

    print(" Sistema Multiespecialista com Quadro Negro e Gerador de Tarefas")

    while True:
        print("\n1. Adicionar nova tarefa manualmente")
        print("2. Gerar tarefa automaticamente")
        print("3. Listar tarefas")
        print("4. Processar tarefas pendentes")
        print("5. Sair")
        opcao = input("Escolha uma opção: ")

        if opcao == "1":
            descricao = input("Descrição da tarefa: ")
            quadro.adicionar_tarefa(descricao)

        elif opcao == "2":
            tarefa = gerador.gerar_tarefa()
            quadro.adicionar_tarefa(tarefa)

        elif opcao == "3":
            quadro.listar_tarefas()

        elif opcao == "4":
            quadro.processar_tarefas(sistema)

        elif opcao == "5" or opcao.lower() == "sair":
            print("Encerrando o sistema. Até mais!")
            break

        else:
            print("Opção inválida.")
