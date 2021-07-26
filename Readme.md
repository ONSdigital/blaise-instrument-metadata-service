# Blaise Instrument Metadata Service

## Setup ##

#### Environment variables ####

* PROJECT_ID

#### Authenticate ####

`gcloud auth application-default login`

#### Start the Flask app ####
`poetry run python main.py`

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

### Get a TO Start Date ###

#### Request ####

`GET` `tostartdate/<questionnaire>` 

#### Response ####


````
Status code: 200
{
    "tostartdate": "2021-06-27T16:29:00+00:00"
}
````

### Create a TO start date ###

#### Request ####

`POST` `tostartdate/<questionnaire>`

_Requires json body of
`{"tostartdate": "yyyy-mm-dd"}`_

#### Response ####

````
Status code: 201
{
    "DST2106A": "2021-08-26T00:00:00"
}
````

### Update a livedate ###

#### Request ####

`PATCH` `tostartdate/<questionnaire>`

_Requires json body of
`{"tostartdate": "yyyy-mm-dd"}`_

#### Response ####

````
Status code: 200
{
    "DST2106A": "2021-08-26T00:00:00"
}
````

### Delete a livedate ###

#### Request ####

`DELETE` `tostartdate/<questionnaire>`

#### Response ####

````
Status code: 204
````
