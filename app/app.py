from flask import Flask, jsonify
from google.cloud.datastore import Client
from werkzeug.exceptions import BadRequest, Conflict, NotFound

from app.tm_release_date import tmreleasedate
from app.to_start_date import tostartdate

app = Flask(__name__)
app.register_blueprint(tostartdate)
app.register_blueprint(tmreleasedate)


def init_datastore(app: Flask, datastore_client: Client, project_id: str):
    app.datastore = DataStore(datastore_client, project_id)


@app.route("/bims/<version>/health")
def health_check(version):
    print(f"Checking {version} health")
    response = {"healthy": True}
    return jsonify(response)


@app.errorhandler(400)
def handle_bad_request(err: BadRequest):
    print(f"Bad Request {err.description}")
    return jsonify({"Bad Request": err.description}), 400


@app.errorhandler(404)
def handle_not_found(err: NotFound):
    print(f"Not found {err.description}")
    return jsonify({"Not Found": err.description}), 404


@app.errorhandler(409)
def handle_conflict(err: Conflict):
    print(f"Already exists {err.description}")
    return jsonify({"Already Exists": err.description}), 409


@app.errorhandler(Exception)
def handle_internal_error(err: Exception):
    print(f"I have an error {err}")
    return jsonify({"error": str(err)}), 500
