
import random
from datetime import datetime, timedelta
from src.api.input.contexto import Contexto


# ############################### Objects


class ContextoDataset:
    def __init__(self, id_cenario, estado_frequencia_cardiaca, atividade, localizacao_semantica, duracao,
                 horario_inicio_final,
                 necessario_alerta_cuidador):
        self.id_cenario = id_cenario
        self.estado_frequencia_cardiaca = estado_frequencia_cardiaca
        self.atividade = atividade
        self.localizacao_semantica = localizacao_semantica
        self.duracao = duracao
        self.horario_inicio_final = horario_inicio_final
        self.necessario_alerta_cuidador = necessario_alerta_cuidador

    def __str__(self):
        return str(self.__class__) + ": " + str(self.__dict__)


class ContextoDatasetRetorno:
    def __init__(self, lista_contextos, lista_resultados_esperados):
        self.lista_contextos = lista_contextos
        self.lista_resultados_esperados = lista_resultados_esperados

    def __str__(self):
        return str(self.__class__) + ": " + str(self.__dict__)


# ############################### Methods


def generate_random_full_scenario():
    """
    Infomações:

    - Regras de execução:
    estado_frequencia_cardiaca: se 3 ou 4 quantidade de aparições == 60
    atividade: se 1 quantidade de aparições == 60
    localizacao_semantica: se 1,2,3,4,5,6,7 ou 8 quantidade de aparições == 60
    duracao: se 1 == 60 vezes se 2 == 120 vezes

    - Campos:
    estado_frequencia_cardiaca: repouso (1), normal (2), agitacaoRegular (3), agitacaoIrregular (4)
    atividade: parado (1), caminhada (2), corrida (3), emVeiculo (4)
    localizacao_semantica: banheiro (1), quarto (2), sala (3), cozinha (4), varanda (5), patio (6), foraPatio (7)
    necessario_alerta_cuidador: 0 == false 1 == true
    """

    # 1
    ataque_disfuncao_psicologica = ContextoDataset(1,
                                                   [3.0, 4.0], [1.0], [1.0, 2.0, 3.0, 4.0, 5.0, 6.0, 7.0],
                                                   [1], [], 1.0)
    # 2
    fuga_sem_acompanhamento = ContextoDataset(2,
                                              [2.0, 3.0], [2.0, 3.0], [5.0, 6.0, 7.0], [1], [], 1)
    # 3
    disfuncao_psicologica_ambiente_desconhecido = ContextoDataset(3,
                                                                  [3.0, 4.0], [1.0, 2.0, 4.0], [7.0, 8.0], [1], [], 1.0)
    # 4
    problema_saude_respiratorio = ContextoDataset(4,
                                                  [4.0], [1.0], [1.0, 2.0, 3.0, 4.0, 5.0, 6.0, 7.0], [1], [], 1.0)
    # 5
    dormindo = ContextoDataset(5,
                               [1.0], [1.0], [2.0, 3.0], [1], [], 0.0)
    # 6
    cenario_normal = ContextoDataset(6,
                                     [2.0], [1.0, 2.0, 4.0], [1.0, 2.0, 3.0, 4.0, 5.0, 6.0, 7.0], [1],
                                     ["08:01:00", "22:59:59"], 0.0)
    # 7
    ataque_saude_convulsao = ContextoDataset(7,
                                             [4.0], [1.0, 2.0, 3.0, 4.0], [1.0, 2.0, 3.0, 4.0, 5.0, 6.0, 7.0],
                                             [2], [], 1.0)
    # 8
    queda_atividades_banho_higiene = ContextoDataset(8,
                                                     [3.0, 4.0], [1.0], [1.0], [1], [], 1.0)
    # 9
    acorda_durante_madrugada_desacompanhado = ContextoDataset(9,
                                                              [2.0, 3.0, 4.0], [1.0, 2.0, 3.0],
                                                              [1.0, 2.0, 3.0, 4.0, 5.0, 6.0], [1],
                                                              ["23:00:00", "08:00:59"], 1.0)
    # 10
    infeccao_corpo_sem_febre = ContextoDataset(10,
                                               [3.0, 4.0], [1.0, 2.0, 3.0, 4.0], [1.0, 2.0, 3.0, 4.0, 5.0, 6.0, 7.0],
                                               [120], [], 1.0)

    cenarios = [ataque_disfuncao_psicologica, fuga_sem_acompanhamento, disfuncao_psicologica_ambiente_desconhecido,
                problema_saude_respiratorio, dormindo, cenario_normal, ataque_saude_convulsao,
                queda_atividades_banho_higiene,
                acorda_durante_madrugada_desacompanhado, infeccao_corpo_sem_febre]

    return random.choice(cenarios)


def generate_random_scenario_sequence(qt_scenarios):
    current_time = datetime.now()
    lista_contextos = []
    lista_resultados_esperados = []

    for x in range(qt_scenarios):

        cenario = generate_random_full_scenario()

        estado_frequencia_cardiaca = random.choice(cenario.estado_frequencia_cardiaca)
        atividade = random.choice(cenario.atividade)
        localizacao_semantica = random.choice(cenario.localizacao_semantica)
        cenario_duracao = random.choice(cenario.duracao)

        lista_resultados_esperados.append(cenario.id_cenario)

        if x == 0:
            current_time = datetime.now()

        current_time = current_time + timedelta(0, 1)

        for y in range(cenario_duracao):
            contextoDuracao = Contexto(cenario.id_cenario, estado_frequencia_cardiaca, atividade, localizacao_semantica,
                                       cenario.necessario_alerta_cuidador, current_time)

            lista_contextos.append(contextoDuracao)

            current_time = current_time + timedelta(0, 1)

    return ContextoDatasetRetorno(lista_contextos, lista_resultados_esperados)


# ############################### Testes


contextos_teste = generate_random_scenario_sequence(6)

print("\n")

print("-------------- Contextos - Quantidade: " + str(len(contextos_teste.lista_contextos)))
for x in contextos_teste.lista_contextos:
    print(x)

print("\n")

print("-------------- Contextos - Resultados esperados")
for x in contextos_teste.lista_resultados_esperados:
    print(x)

print("\n")