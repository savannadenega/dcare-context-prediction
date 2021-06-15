
import logging
import schedule
from src.contextprediction import context_prediction
from src.api import api
from src.contextidentification import context_identification


def main():
    schedule.every(5).seconds.do(run_schedule_dcare_tasks())


def run_schedule_dcare_tasks():
    logging.info("Running scheduler DCARE tasks project")
    api.request_iot_data()
    context_prediction.train()
    context_prediction.predict()
    context_identification.validate_necessary_post_danger_alert_patient("patient_id", "context_id")


if __name__ == "__main__":
    main()