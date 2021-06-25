## Blaise Instrument Metadata Service

###Install dependencies <br>
`poetry install`

###**Run tests <br>**
Behave <br>
`poetry run python -m behave tests/features`<br>

Pytest <br>
`poetry run python -m pytest`

API Help

`livedate/<questionnaire>/create`
Requires json body of
`{"livedate": "25/06/2021"}`

`livedate/<questionnaire>`
Gets a live date for a questionnaire

`livedate/<questionnaire>/delete`
deletes a live date for a questionnaire