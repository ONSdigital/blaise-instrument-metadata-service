from flask import Flask, jsonify, request, current_app

from api import livedate
from data_sources.datastore import DataStore


api = Flask(__name__)
api.register_blueprint(livedate)


def init_datastore(app: Flask, datastore: DataStore):
    app.datastore = datastore


@api.errorhandler(400)
def error_handler(err: Exception):
    return jsonify({"error": err.description}), 400


@api.errorhandler(Exception)
def error_handler(err: Exception):
    return jsonify({"error": str(err)}), 500

@api.route("/bims/<version>/health")
def health_check(version):
    print(f"Checking {version} health")   
    response = {"healthy": True}
    return jsonify(response)
