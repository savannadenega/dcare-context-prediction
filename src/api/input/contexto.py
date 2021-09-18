class Contexto:
    def __init__(self, id_cenario, estado_frequencia_cardiaca, atividade, localizacao_semantica,
                 necessario_alerta_cuidador, data_hora):
        self.id_cenario = id_cenario
        self.estado_frequencia_cardiaca = estado_frequencia_cardiaca
        self.atividade = atividade
        self.localizacao_semantica = localizacao_semantica
        self.necessario_alerta_cuidador = necessario_alerta_cuidador
        self.data_hora = data_hora

    def __str__(self):
        return str(self.__class__) + ": " + str(self.__dict__)
