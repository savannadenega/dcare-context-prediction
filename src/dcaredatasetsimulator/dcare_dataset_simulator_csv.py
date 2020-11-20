import csv
import os
from pathlib import Path
from src.dcaredatasetsimulator.dcare_dataset_simulator import generate_random_scenario_sequence
import time

def generate_scenarios_to_csv(qt_scenarious):
    contextos = generate_random_scenario_sequence(qt_scenarious)
    contexto_dataset = contextos.lista_contextos
    num_contextos = len(contexto_dataset)

    row_list = []

    line1 = ["", "labels"]
    for x in range(num_contextos):
        x = x + 2
        line1.append(x+2)

    row_list.append(line1)

    n = 100
    lista_id_cenario = []
    lista_estado_frequencia_cardiaca = []
    lista_atividade = []
    lista_localizacao_semantica = []
    lista_necessario_alerta_cuidador = []

    for contexto in contexto_dataset:
        lista_id_cenario.append(contexto.id_cenario)
        lista_estado_frequencia_cardiaca.append(contexto.estado_frequencia_cardiaca)
        lista_atividade.append(contexto.atividade)
        lista_localizacao_semantica.append(contexto.localizacao_semantica)
        lista_necessario_alerta_cuidador.append(contexto.necessario_alerta_cuidador)

    line_id_cenario = [n, 1]
    n = n + 1
    list = line_id_cenario + lista_id_cenario

    for x in range(5):
        row_list.append(list)

    line_estado_frequencia_cardiaca = [n, 2]
    n = n + 1
    list = line_estado_frequencia_cardiaca + lista_estado_frequencia_cardiaca
    for x in range(5):
        row_list.append(list)

    line_atividade = [n, 4]
    n = n + 1
    list = line_atividade + lista_atividade
    for x in range(5):
        row_list.append(list)

    line_localizacao_semantica = [n, 3]
    n = n + 1
    list = line_localizacao_semantica + lista_localizacao_semantica
    for x in range(5):
        row_list.append(list)

    line_necessario_alerta_cuidador = [n, 5]
    list = line_necessario_alerta_cuidador + lista_necessario_alerta_cuidador
    for x in range(5):
        row_list.append(list)

    dirname = Path(__file__).parent.parent
    filename = os.path.join(dirname, 'db/dataset.csv')
    with open(filename, 'w', newline='') as file:
        writer = csv.writer(file)
        writer.writerows(row_list)


generate_scenarios_to_csv(602)
