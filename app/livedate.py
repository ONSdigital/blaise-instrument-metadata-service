from datetime import datetime

from flask import Blueprint, request, current_app, jsonify, abort

livedate = Blueprint("livedate", __name__, url_prefix="/livedate")


@livedate.route("/<questionnaire>")
def get_live_date_for_questionnaire(questionnaire: str):
    livedate = current_app.datastore.get_livedate(questionnaire)
    if livedate is None:
        abort(404, description=f"No data found for {questionnaire}")
    return jsonify(livedate), 200


@livedate.route("/<questionnaire>/create", methods=["POST"])
def create_live_date_for_a_questionnaire(questionnaire: str):
    try:
        request_data = request.get_json()
    except:
        abort(400, description="Requires JSON format")

    if "livedate" not in request_data:
        abort(400, description="livedate is required, in format dd/mm/yyyy")
    live_date = request_data["livedate"]

    try:
        formatted_date = datetime.strptime(live_date, "%d/%m/%Y")
    except ValueError:
        abort(400, description="Date is not in the required format dd/mm/yyyy")

    livedate = current_app.datastore.get_livedate(questionnaire)
    if livedate is not None:
        abort(409, description=f"{questionnaire} already has a live date {livedate}. Please use the Patch end point "
                               f"to update the livedate")

    result = current_app.datastore.add_livedate(questionnaire, formatted_date)
    return jsonify(result), 201


@livedate.route("/<questionnaire>/update", methods=["PATCH"])
def update_live_date_for_a_questionnaire(questionnaire: str):
    try:
        request_data = request.get_json()
    except:
        abort(400, description="Requires JSON format")

    if "livedate" not in request_data:
        abort(400, description="livedate is required, in format dd/mm/yyyy")
    live_date = request_data["livedate"]

    try:
        formatted_date = datetime.strptime(live_date, "%d/%m/%Y")
    except ValueError:
        abort(400, description="Date is not in the required format dd/mm/yyyy")

    livedate = current_app.datastore.get_livedate(questionnaire)
    if livedate is None:
        abort(400, description=f"No data found for {questionnaire}, please use the create end point")

    result = current_app.datastore.add_livedate(questionnaire, formatted_date)
    return jsonify(result), 200


@livedate.route("/<questionnaire>/delete", methods=["DELETE"])
def delete_live_date_from_questionnaire(questionnaire):
    livedate = current_app.datastore.get_livedate(questionnaire)
    if livedate is None:
        abort(404, description=f"No data found for {questionnaire}")
    current_app.datastore.delete_livedate(questionnaire)
    return f"Deleted {questionnaire}", 204
