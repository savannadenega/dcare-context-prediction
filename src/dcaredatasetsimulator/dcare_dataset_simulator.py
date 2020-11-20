import os
import random
from pathlib import Path
from datetime import datetime, timedelta

from src.api.input.contexto import Contexto


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


class ContextoDataseRetorno:
    def __init__(self, lista_contextos, lista_resultados_esperados):
        self.lista_contextos = lista_contextos
        self.lista_resultados_esperados = lista_resultados_esperados


def generate_random_full_scenario():
    # estado_frequencia_cardiaca: se 3 ou 4 quantidade de aparições == 60
    # atividade: se 1 quantidade de aparições == 60
    # localizacao_semantica: se 1,2,3,4,5,6,7 ou 8 quantidade de aparições == 60
    # duracao: se 1 == 60 vezes se 2 == 120 vezes

    # possibilidades: repouso (1), normal (2), agitacaoRegular (3), agitacaoIrregular (4)
    # possibilidades: parado (1), caminhada (2), corrida (3), emVeiculo (4)
    # possibilidades: banheiro (1), quarto (2), sala (3), cozinha (4), varanda (5), patio (6), foraPatio (7)

    ataque_disfuncao_psicologica = ContextoDataset("ataque_disfuncao_psicologica",
                                                   [3, 4], [1], [1, 2, 3, 4, 5, 6, 7], [1], [], True)
    fuga_sem_acompanhamento = ContextoDataset("fuga_sem_acompanhamento",
                                              [2, 3], [2, 3], [5, 6, 7], [1], [], True)
    disfuncao_psicologica_ambiente_desconhecido = ContextoDataset("disfuncao_psicologica_ambiente_desconhecido",
                                                                  [3, 4], [1, 2, 4], [7, 8], [1], [], True)
    problema_saude_respiratorio = ContextoDataset("problema_saude_respiratorio",
                                                  [4], [1], [1, 2, 3, 4, 5, 6, 7], [1], [], True)
    dormindo = ContextoDataset("dormindo",
                               [1], [1], [2, 3], [1], [], False)
    cenario_normal = ContextoDataset("cenario_normal",
                                     [2], [1, 2, 4], [1, 2, 3, 4, 5, 6, 7], [1], ["08:01:00", "22:59:59"], False)
    ataque_saude_convulsao = ContextoDataset("ataque_saude_convulsao",
                                             [4], [1, 2, 3, 4], [1, 2, 3, 4, 5, 6, 7], [2], [], True)
    queda_atividades_banho_higiene = ContextoDataset("queda_atividades_banho_higiene",
                                                     [3, 4], [1], [1], [1], [], True)
    acorda_durante_madrugada_desacompanhado = ContextoDataset("acorda_durante_madrugada_desacompanhado",
                                                              [2, 3, 4], [1, 2, 3], [1, 2, 3, 4, 5, 6], [1],
                                                              ["23:00:00", "08:00:59"], True)
    infeccao_corpo_sem_febre = ContextoDataset("infeccao_corpo_sem_febre",
                                               [3, 4], [1, 2, 3, 4], [1, 2, 3, 4, 5, 6, 7], [120], [], True)

    cenarios = [ataque_disfuncao_psicologica, fuga_sem_acompanhamento, disfuncao_psicologica_ambiente_desconhecido,
                problema_saude_respiratorio, dormindo, cenario_normal, ataque_saude_convulsao,
                queda_atividades_banho_higiene,
                acorda_durante_madrugada_desacompanhado, infeccao_corpo_sem_febre]

    return random.choice(cenarios)
    # return infeccao_corpo_sem_febre


def generate_random_scenario_sequence(qt_scenarios):
    global current_time
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
            contextoDuracao = Contexto(estado_frequencia_cardiaca, atividade, localizacao_semantica,
                                       cenario.necessario_alerta_cuidador, current_time)

            lista_contextos.append(contextoDuracao)

            current_time = current_time + timedelta(0, 1)

    return ContextoDataseRetorno(lista_contextos, lista_resultados_esperados)

### Execucao

contextos_teste = generate_random_scenario_sequence(6)

print(contextos_teste)
