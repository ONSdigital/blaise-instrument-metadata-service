from datetime import datetime

from flask import Blueprint, request, current_app, jsonify, abort
from poetry.core.utils._compat import urlparse

from app.util import get_current_url

livedate = Blueprint("livedate", __name__, url_prefix="/livedate")


@livedate.route("/<questionnaire>")
def get_live_date_for_questionnaire(questionnaire: str):
    livedate = current_app.datastore.get_livedate(questionnaire)
    if livedate is None:
        abort(404, description=f"No data found for {questionnaire}")
    return jsonify(livedate), 200


@livedate.route("/<questionnaire>", methods=["POST"])
def create_live_date_for_a_questionnaire(questionnaire: str):
    formatted_date = get_formatted_date(request)

    livedate = current_app.datastore.get_livedate(questionnaire)
    if livedate is not None:
        abort(409, description=f"{questionnaire} already has a live date {livedate}. Please use the Patch end point "
                               f"to update the livedate")

    result = current_app.datastore.add_livedate(questionnaire, formatted_date)
    current_url = get_current_url(request)
    return jsonify({"location": f"{current_url}/livedate/{questionnaire}"}), 201


@livedate.route("/<questionnaire>", methods=["PATCH"])
def update_live_date_for_a_questionnaire(questionnaire: str):
    formatted_date = get_formatted_date(request)

    livedate = current_app.datastore.get_livedate(questionnaire)
    if livedate is None:
        abort(400, description=f"No data found for {questionnaire}, please use the create end point")

    current_app.datastore.add_livedate(questionnaire, formatted_date)
    current_url = get_current_url(request)
    return jsonify({"location": f"{current_url}/livedate/{questionnaire}"}), 200


@livedate.route("/<questionnaire>", methods=["DELETE"])
def delete_live_date_from_questionnaire(questionnaire):
    livedate = current_app.datastore.get_livedate(questionnaire)
    if livedate is None:
        abort(404, description=f"No data found for {questionnaire}")
    current_app.datastore.delete_livedate(questionnaire)
    return f"Deleted {questionnaire}", 204


def get_formatted_date(request_body):
    try:
        request_data = request_body.get_json()
        if request_data is None:
            raise
    except:
        abort(400, description="Requires JSON format")

    if "livedate" not in request_data:
        abort(400, description="livedate is required, in format yyyy-mm-dd")
    live_date = request_data["livedate"]

    try:
        formatted_date = datetime.strptime(live_date, "%Y-%m-%d")
    except ValueError:
        abort(400, description="Date is not in the required format yyyy-mm-dd")

    return formatted_date
