
import logging
from src.queue import queue_manager


def identify_behaviors(iot_data_response):
    logging.info("Running behaviors identifier...")
    # TODO configurar identificacao de comportamentos/contextos
    validate_necessary_post_danger_alert_patient("patient_id", "context_id")


def validate_necessary_post_danger_alert_patient(patient_id, context_id):
    logging.info("Running validate_necessary_post_danger_alert_patient...")
    # TODO busca dados no DB
    # TODO realiza validação dos dados sobre necessidade de alerta ao paciente
    queue_manager.post_danger_alert_patient("ID", "True")

