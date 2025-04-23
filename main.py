from blackboard.Bancada import Bancada
from especialista.Atendente import Atendente
from especialista.Triagem import Triagem
from especialista.EngEletrico import EngEletrico
from especialista.Suporte import Suporte
from especialista.Tecnico import Tecnico
from especialista.Estagiario import Estagiario
from especialista.Eletricista import Eletricista
from especialista.Testador import Testador
from especialista.Finalizador import Finalizador
from geradordetarefa.GeradorDeTarefa import GeradorDeTarefa
from controlador.Controlador import Controlador

# Inicializando a bancada
bancada = Bancada()

gerador = GeradorDeTarefa(bancada)
triagem = Triagem(gerador)

# Inicializando os especialistas
especialistas = [Atendente(), Triagem(gerador), Tecnico(), Estagiario(), EngEletrico(), Eletricista(), Suporte(), Testador(), Finalizador()]

# Registrando especialistas na bancada
for esp in especialistas:
    esp.Bancada = bancada
    bancada.adicionaEspecialista(esp)

# Executa o sistema com o controlador
controlador = Controlador(bancada, gerador)
contribuicoes = controlador.loop()

# Exibe o resultado
print("\n--- RESULTADO FINAL ---")
print("Progresso:", bancada.estadoCompartilhado['progresso'])
print("Contribuições:")
for x in contribuicoes:
    try:
        #
        if x[0][1] is None:
            continue
    #Caso a estrutura não seja esperada, ignora
    except (IndexError, TypeError):
        continue
    print(x)
