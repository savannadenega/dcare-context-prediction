
import logging


def check_danger_alert_patient(patient_id):
    logging.info("Method check_danger_alert_patient")
    return True
    # TODO configurar


def post_danger_alert_patient(patient_id, data):
    logging.info("Method post_danger_alert_patient")
    # TODO configurar


class Response:
    def __init__(self, id, enviarAlertaCuidador):
        self.id = id
        self.enviarAlertaCuidador = enviarAlertaCuidador