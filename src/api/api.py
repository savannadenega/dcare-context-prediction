# app.config["DEBUG"] = True
import requests
import logging
from flask import Flask, request, jsonify
from src.queue import queue_manager
from src.contextidentification import context_identification

app = Flask(__name__)


@app.route('/v1/checkDangerAlertPatient', methods=['GET'])
def return_check_danger_alert_patient():
    patient_id = request.args.get('id', type=int)  # ?id=3
    if patient_id is None:
        logging.info("Received request to checkDangerAlertPatient without patient_id")
        return jsonify(isError=True,
                       message="Error: No id field provided. Please specify a patient id.",
                       statusCode=500)
    else:

        logging.info("Received request to checkDangerAlertPatient of patient id: " + str(patient_id))
        response_data = queue_manager.check_danger_alert_patient(patient_id)

        return jsonify(isError=False,
                       message="Success",
                       statusCode=200,
                       data=response_data)


def request_iot_data(url):
    iot_data_response = requests.get(url)
    logging.info("Requesting data to IoT Wearable from URL: " + url)
    if iot_data_response.ok:
        logging.info("Received data from IoT Wearable - URL: " + url)
        context_identification.identify_behaviors(iot_data_response)
    else:
        logging.info("Error on requesting data from IoT Wearable - URL: " + url)


app.run()
