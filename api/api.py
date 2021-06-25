from flask import Flask, jsonify, request, current_app
from google.cloud.datastore import Client

from api import livedate
from data_sources.datastore import DataStore

api = Flask(__name__)
api.register_blueprint(livedate)


def init_datastore(app: Flask, datastore_client: Client, project_id: int):
    app.datastore = DataStore(datastore_client, project_id)


@api.route("/<questionnaire>")
def get_live_date_for_questionnaire(questionnaire: str):
    livedate = current_app.datastore.get_livedate(questionnaire)
    return jsonify(livedate), 200


@api.errorhandler(400)
def error_handler(err: Exception):
    return jsonify({"error": err.description}), 400


@api.errorhandler(Exception)
def error_handler(err: Exception):
    return jsonify({"error": str(err)}), 500



