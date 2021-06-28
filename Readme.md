# Blaise Instrument Metadata Service

## Setup ##

#### Environment variables ####

* PROJECT_ID

#### Authenticate ####

`gcloud auth application-default login`

#### Start the Flask app ####
`poetry run pythin main.py`

## Install dependencies ####

`poetry install`

`poetry update`

## Run tests ##

#### Run All tests ####

`make test`

#### Behave ####

`poetry run python -m behave tests/features`<br>

#### Pytest ####

`poetry run python -m pytest`

## Rest API ##

### Get a Live date ###

#### Request ####

`GET` `livedate/<questionnaire>` 

#### Response ####


````
Status code: 200
{
    "livedate": "2021-06-27T16:29:00+00:00"
}
````

### Create a livedate ###

#### Request ####

`POST` `livedate/<questionnaire>/create`

_Requires json body of
`{"livedate": "25/06/2021"}`_

#### Response ####

````
Status code: 201
{
    "DST2106A": "2021-08-26T00:00:00"
}
````

### Update a livedate ###

#### Request ####

`PATCH` `livedate/<questionnaire>/create`

_Requires json body of
`{"livedate": "26/06/2021"}`_

#### Response ####

````
Status code: 200
{
    "DST2106A": "2021-08-26T00:00:00"
}
````

### Delete a livedate ###

#### Request ####

`DELETE` `livedate/<questionnaire>/delete`

#### Response ####

````
Status code: 204
````
