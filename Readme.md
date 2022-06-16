# Blaise Instrument Metadata Service

## Setup ##

#### Environment variables ####

Export the PROJECT_ID variable.  For Mac users execute the following, where <sandbox> is your sandbox name:

`export PROJECT_ID=ons-blaise-v2-dev-<sandbox>`

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

### Get a TM Release Date ###

#### Request ####

`GET` `tmreleasedate/<questionnaire>`

#### Response ####


````
Status code: 200
{
    "tmreleasedate": "2021-06-27T16:29:00+00:00"
}
````

### Create a TM Release date ###

#### Request ####

`POST` `tmreleasedate/<questionnaire>`

_Requires json body of
`{"tmreleasedate": "yyyy-mm-dd"}`_

#### Response ####

````
Status code: 201
{
    "DST2106A": "2021-08-26T00:00:00"
}
````

### Update a release date ###

#### Request ####

`PATCH` `tostartdate/<questionnaire>`

_Requires json body of
`{"tmreleasedate": "yyyy-mm-dd"}`_

#### Response ####

````
Status code: 200
{
    "DST2106A": "2021-08-26T00:00:00"
}
````

### Delete a release date ###

#### Request ####

`DELETE` `tmreleasedate/<questionnaire>`

#### Response ####

````
Status code: 204
````
