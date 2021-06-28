import json

from behave import given, then, when
from datetime import datetime


@given(u'datastore contains')
def step_impl(context):
    for row in context.table:
        context.datastore.add_livedate(row["questionnaire"], datetime.strptime(row["livedate"], "%d-%m-%Y"))


@when(u'I Get "{path}":')
def step_impl(context, path):
    response = context.client.get(path, content_type="application/json")
    context.response = response.get_json()
    context.response_status_code = response.status_code


@when(u'I POST "{path}" with the payload')
def step_impl(context, path):
    response = context.client.post(
        path, data=context.text, content_type="application/json"
    )
    context.response = response.get_json()
    context.response_status_code = response.status_code


@when(u'I Delete "{path}":')
def step_impl(context, path):
    response = context.client.delete(path, content_type="application/json")
    context.response = response.get_json()
    context.response_status_code = response.status_code


@when(u'I PATCH "{path}" with the payload')
def step_impl(context, path):
    response = context.client.patch(
        path, data=context.text, content_type="application/json"
    )
    context.response = response.get_json()
    context.response_status_code = response.status_code


@then(u'datastore should contain')
def step_impl(context):
    context.datastore.store
    for row in context.table:
        key = row["key"]
        if key not in context.datastore.store:
            raise Exception(f"Expected key '{key}' not found in datastore")
        assert datetime.strptime(row["livedate"], "%d-%m-%Y") == context.datastore.store[key]["livedate"]
        assert row["questionnaire"] == context.datastore.store[key]["questionnaire"]


@then(u'the response code should be "{status_code}"')
def step_impl(context, status_code):
    assert context.response_status_code == int(status_code), (
            f"Response code {context.response_status_code}"
            + " did not match expected value: {status_code}"
    )


@then(u'the response should be')
def step_impl(context):
    assert context.response == json.loads(context.text), f"Response {context.response} does not match {context.text}"
