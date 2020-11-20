import os
from pathlib import Path

quant_cenarios = 2

def generate_scenarios_to_txt():
    dirname = Path(__file__).parent.parent
    filename = os.path.join(dirname, 'db/dataset.txt')
    dataset_object = open(filename, "w")
    contextos = []

    for x in range(quant_cenarios):
        # possibilidades: normal (1), repouso (2), agitacaoRegular (3), agitacaoIrregular (4)
        estado_frequencia_cardiaca = 3

        # possibilidades: parado (1), caminhada (2), corrida (3), emVeiculo (4)
        atividade = 3

        # possibilidades: banheiro (1), quarto (2), sala (3), cozinha (4),
        # cozinha (5), varanda (6), patio (7), foraPatio (8)
        localizacao_semantica = 3

        item = "{}-{}-{}\n"
        contextos.append(item.format(estado_frequencia_cardiaca, atividade, localizacao_semantica))

    dataset_object.writelines(contextos)
    dataset_object.close()