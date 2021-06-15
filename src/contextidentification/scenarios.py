

################################ Fields

estado_frequencia_cardiaca = {
  "repouso": 1,
  "normal": 2,
  "agitacaoRegular": 3,
  "agitacaoIrregular": 4
}

estado_frequencia_cardiaca_id = {
  "1": "repouso",
  "2": "normal",
  "3": "agitacaoRegular",
  "4": "agitacaoIrregular"
}

atividade = {
  "parado": 1,
  "caminhada": 2,
  "corrida": 3,
  "emVeiculo": 4
}

atividade_id = {
  "1": "parado",
  "2": "caminhada",
  "3": "corrida",
  "4": "emVeiculo"
}

localizacao_semantica = {
  "banheiro": 1,
  "quarto": 2,
  "sala": 3,
  "cozinha": 4,
  "varanda": 5,
  "patio": 6,
  "foraPatio": 7
}

localizacao_semantica_id = {
  "1": "banheiro",
  "2": "quarto",
  "3": "sala",
  "4": "cozinha",
  "5": "varanda",
  "6": "patio",
  "7": "foraPatio"
}

necessario_alerta_cuidador = {
  "false": 0,
  "true": 1
}

necessario_alerta_cuidador_id = {
  "0": "false",
  "1": "true"
}


################################ Scenarios


all_scenarios = [ataque_disfuncao_psicologica_1, fuga_sem_acompanhamento_2, disfuncao_psicologica_ambiente_desconhecido_3,
    problema_saude_respiratorio_4, dormindo_5, cenario_normal_6, ataque_saude_convulsao_7, queda_atividades_banho_higiene_8,
    acorda_durante_madrugada_desacompanhado_9, infeccao_corpo_sem_febre_10]


ataque_disfuncao_psicologica_1 = {
  "id_cenario": 1,
  "descricao_cenario": "ataque_disfuncao_psicologica",
  "estado_frequencia_cardiaca": {"agitacaoRegular", "agitacaoIrregular"},
  "atividade": {"parado"},
  "localizacao_semantica": {"banheiro", "quarto", "sala", "cozinha", "varanda", "patio", "foraPatio"},
  "duracao": 1,
  "horario_inicio_final": {},
  "necessario_alerta_cuidador": 1
}

fuga_sem_acompanhamento_2 = {
  "id_cenario": 2,
  "descricao_cenario": "fuga_sem_acompanhamento",
  "estado_frequencia_cardiaca": {"normal", "agitacaoRegular"},
  "atividade": {"caminhada", "corrida"},
  "localizacao_semantica": {"varanda", "patio", "foraPatio"},
  "duracao": 1,
  "horario_inicio_final": {},
  "necessario_alerta_cuidador": 1
}

disfuncao_psicologica_ambiente_desconhecido_3 = {
  "id_cenario": 3,
  "descricao_cenario": "disfuncao_psicologica_ambiente_desconhecido",
  "estado_frequencia_cardiaca": {"agitacaoRegular", "agitacaoIrregular"},
  "atividade": {"parado", "caminhada", "emVeiculo"},
  "localizacao_semantica": {"foraPatio"},
  "duracao": 1,
  "horario_inicio_final": {},
  "necessario_alerta_cuidador": 1
}

problema_saude_respiratorio_4 = {
  "id_cenario": 4,
  "descricao_cenario": "disfuncao_psicologica_ambiente_desconhecido",
  "estado_frequencia_cardiaca": {"agitacaoIrregular"},
  "atividade": {"parado"},
  "localizacao_semantica": {"banheiro", "quarto", "sala", "cozinha", "varanda", "patio", "foraPatio"},
  "duracao": 1,
  "horario_inicio_final": {},
  "necessario_alerta_cuidador": 1
}

dormindo_5 = {
  "id_cenario": 5,
  "descricao_cenario": "dormindo",
  "estado_frequencia_cardiaca": {"repouso"},
  "atividade": {"parado"},
  "localizacao_semantica": {"quarto", "sala"},
  "duracao": 1,
  "horario_inicio_final": {},
  "necessario_alerta_cuidador": 0
}

cenario_normal_6 = {
  "id_cenario": 6,
  "descricao_cenario": "cenario_normal",
  "estado_frequencia_cardiaca": {"normal"},
  "atividade": {"parado", "caminhada", "emVeiculo"},
  "localizacao_semantica": {"banheiro", "quarto", "sala", "cozinha", "varanda", "patio", "foraPatio"},
  "duracao": 1,
  "horario_inicio_final": {"08:01:00", "22:59:59"},
  "necessario_alerta_cuidador": 0
}

ataque_saude_convulsao_7 = {
  "id_cenario": 7,
  "descricao_cenario": "ataque_saude_convulsao",
  "estado_frequencia_cardiaca": {"agitacaoIrregular"},
  "atividade": {"parado", "caminhada", "corrida", "emVeiculo"},
  "localizacao_semantica": {"banheiro", "quarto", "sala", "cozinha", "varanda", "patio", "foraPatio"},
  "duracao": 2,
  "horario_inicio_final": {},
  "necessario_alerta_cuidador": 1
}

queda_atividades_banho_higiene_8 = {
  "id_cenario": 8,
  "descricao_cenario": "queda_atividades_banho_higiene",
  "estado_frequencia_cardiaca": {"agitacaoRegular", "agitacaoIrregular"},
  "atividade": {"parado"},
  "localizacao_semantica": {"banheiro"},
  "duracao": 1,
  "horario_inicio_final": {},
  "necessario_alerta_cuidador": 1
}

acorda_durante_madrugada_desacompanhado_9 = {
  "id_cenario": 9,
  "descricao_cenario": "acorda_durante_madrugada_desacompanhado",
  "estado_frequencia_cardiaca": {"normal", "agitacaoRegular", "agitacaoIrregular"},
  "atividade": {"parado", "caminhada", "corrida"},
  "localizacao_semantica": {"banheiro", "quarto", "sala", "cozinha", "varanda", "patio"},
  "duracao": 1,
  "horario_inicio_final": {"23:00:00", "08:00:59"},
  "necessario_alerta_cuidador": 1
}

infeccao_corpo_sem_febre_10 = {
  "id_cenario": 10,
  "descricao_cenario": "infeccao_corpo_sem_febre",
  "estado_frequencia_cardiaca": {"agitacaoRegular", "agitacaoIrregular"},
  "atividade": {"parado", "caminhada", "corrida", "emVeiculo"},
  "localizacao_semantica": {"banheiro", "quarto", "sala", "cozinha", "varanda", "patio", "foraPatio"},
  "duracao": 120,
  "horario_inicio_final": {},
  "necessario_alerta_cuidador": 1
}
