import random

class GeradorDeTarefa:
    def __init__(self):
        self.modelos_tarefas = [
            "revisar texto do capítulo 1",
            "corrigir erros gramaticais no prefácio",
            "criar sinopse para o novo livro infantil",
            "definir preço de capa para o livro de poesia",
            "planejar campanha de divulgação nas redes sociais",
            "agendar distribuição para as livrarias",
            "calcular faturamento do mês",
            "atualizar estoque do livro 'A Jornada do Herói'",
            "analisar viabilidade de reimpressão",
            "verificar pagamentos pendentes dos autores"
        ]

    def gerar_tarefa(self):
        return random.choice(self.modelos_tarefas)

    def gerar_varias(self, n=3):
        return random.sample(self.modelos_tarefas, min(n, len(self.modelos_tarefas)))
