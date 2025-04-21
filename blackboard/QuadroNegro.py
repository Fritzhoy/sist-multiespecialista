import uuid

class Tarefa:
    def __init__(self, descricao):
        self.id = str(uuid.uuid4())[:8]
        self.descricao = descricao
        self.status = "pendente"
        self.resposta = None
        self.responsavel = None

class QuadroNegro:
    def __init__(self):
        self.tarefas = []
        self.contribuicoes = []

    def adicionar_contribuicao(self, tarefa_id, especialista, contribuicao):
        self.contribuicoes.append({
            "tarefa_id": tarefa_id,
            "especialista": especialista,
            "contribuicao": contribuicao
        })

    def listar_contribuicoes(self):
        print("\n Contribuições registradas:")
        for c in self.contribuicoes:
            print(f" Tarefa {c['tarefa_id']} — {c['especialista']}: {c['contribuicao']}")

    def adicionar_tarefa(self, descricao):
        tarefa = Tarefa(descricao)
        self.tarefas.append(tarefa)
        print(f"Tarefa adicionada com ID {tarefa.id}")

    def listar_tarefas(self, status=None):
        print("\n Tarefas no Quadro:")
        for t in self.tarefas:
            if status is None or t.status == status:
                print(f"[{t.status.upper()}] {t.id}: {t.descricao}")
            if t.resposta:
                print(f"   Resposta: {t.resposta}")
            if t.responsavel:
                print(f"    Feito por: {t.responsavel}")

    def processar_tarefas(self, sistema_especialista):
        for tarefa in self.tarefas:
            if tarefa.status == "pendente":
                resposta, especialista = sistema_especialista.processar_tarefa_com_autor(tarefa.descricao)
                tarefa.resposta = resposta
                tarefa.responsavel = especialista
                tarefa.status = "concluída"
                print(f" Tarefa {tarefa.id} processada pelo: {tarefa.responsavel}")