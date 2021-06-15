
import mysql.connector
import logging

mydb = mysql.connector.connect(
  host="https://www.localhost:8080",
  user="dcare",
  password="dcare",
  database="dcare"
)
mycursor = mydb.cursor()


def insert_context(context):
    sql = "INSERT INTO context (id_cenario, descricao_cenario, estado_frequencia_cardiaca, " \
          "atividade, localizacao_semantica, duracao, " \
          "horario_inicio_final, necessario_alerta_cuidador) VALUES (%s, %s, %s, %s, %s, %s, %s)"
    val = (context["id_cenario"], context["descricao_cenario"], context["estado_frequencia_cardiaca"],
           context["atividade"], context["localizacao_semantica"], context["duracao"],
           context["horario_inicio_final"], context["necessario_alerta_cuidador"])
    mycursor.execute(sql, val)
    mydb.commit()
    logging.info("Context inserted on MySQL DB.")


def get_context_by_id(id_cenario):
    mycursor.execute("SELECT " + id_cenario + " FROM context")
    logging.info("Getting context from MySQL DB of patient id: " + id_cenario)
    return mycursor.fetchall()
