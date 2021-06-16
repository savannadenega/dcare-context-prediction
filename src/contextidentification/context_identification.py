
import logging
from src.queue import queue_manager
from src.api.input.contexto import Contexto


def identify_behaviors(iot_data_response: Contexto):
    logging.info("Running behaviors identifier...")
    # TODO configurar identificacao de comportamentos/contextos
    # iot_data_response["necessario_alerta_cuidador"]
    validate_necessary_post_danger_alert_patient("patient_id", "context_id")


def validate_necessary_post_danger_alert_patient(patient_id, context_id):
    logging.info("Running validate_necessary_post_danger_alert_patient...")
    # TODO busca dados no DB
    # TODO realiza validação dos dados sobre necessidade de alerta ao paciente
    queue_manager.post_danger_alert_patient("ID", "True")

