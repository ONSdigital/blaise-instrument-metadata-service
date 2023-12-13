from unittest import mock

from google.cloud import datastore
from google.cloud.datastore import Key

from data_sources.datastore import DataStore


# Mock_datastore, questionnaire, live_date come from conftest.py
def test_add_to_start_date_with_valid_fields(
    mock_datastore, questionnaire, to_start_date
):
    mocked_key = mock.MagicMock(name=questionnaire.upper())
    mock_datastore.key.return_value = mocked_key
    data_source = DataStore(client=mock_datastore, project_id="foo")
    mock_entity = datastore.Entity(key=mocked_key)
    mock_entity["questionnaire"] = questionnaire.upper()
    mock_entity["tostartdate"] = to_start_date

    assert data_source.add_to_start_date(questionnaire, to_start_date) == {
        questionnaire.upper(): to_start_date.isoformat()
    }
    mock_datastore.key.assert_called_once_with("ToStartDate", questionnaire.upper())
    mock_datastore.put.assert_called_once_with(mock_entity)


def test_get_to_start_date_with_valid_fields(
    mock_datastore, questionnaire, to_start_date
):
    # arrange
    mocked_key = mock.MagicMock(name=questionnaire.upper())
    mock_entity = datastore.Entity(key=mocked_key)
    mock_entity["questionnaire"] = questionnaire.upper()
    mock_entity["tostartdate"] = to_start_date
    mock_datastore.get.return_value = mock_entity
    data_source = DataStore(client=mock_datastore, project_id="foo")

    # act assert
    assert data_source.get_to_start_date(questionnaire) == {
        "tostartdate": to_start_date.isoformat()
    }
    mock_datastore.get.assert_called_once_with(
        Key("ToStartDate", questionnaire.upper(), project="foo")
    )


def test_delete_questionnaire_to_start_date_with_valid_fields(
    mock_datastore, questionnaire, to_start_date
):
    mocked_key = mock.MagicMock(name=questionnaire.upper())
    mock_entity = datastore.Entity(key=mocked_key)
    mock_entity["questionnaire"] = questionnaire.upper()
    mock_entity["tostartdate"] = to_start_date
    mock_datastore.get.return_value = mock_entity
    data_source = DataStore(client=mock_datastore, project_id="foo")

    data_source.delete_to_start_date(questionnaire)
    mock_datastore.delete.assert_called_once_with(mock_entity)


def test_add_tm_release_date_with_valid_fields(
    mock_datastore, questionnaire, tm_release_date
):
    mocked_key = mock.MagicMock(name=questionnaire.upper())
    mock_datastore.key.return_value = mocked_key
    data_source = DataStore(client=mock_datastore, project_id="foo")
    mock_entity = datastore.Entity(key=mocked_key)
    mock_entity["questionnaire"] = questionnaire.upper()
    mock_entity["tmreleasedate"] = tm_release_date

    assert data_source.add_tm_release_date(questionnaire, tm_release_date) == {
        questionnaire.upper(): tm_release_date.isoformat()
    }
    mock_datastore.key.assert_called_once_with("TmReleaseDate", questionnaire.upper())
    mock_datastore.put.assert_called_once_with(mock_entity)


def test_get_tm_release_date_with_valid_fields(
    mock_datastore, questionnaire, tm_release_date
):
    # arrange
    mocked_key = mock.MagicMock(name=questionnaire.upper())
    mock_entity = datastore.Entity(key=mocked_key)
    mock_entity["questionnaire"] = questionnaire.upper()
    mock_entity["tmreleasedate"] = tm_release_date
    mock_datastore.get.return_value = mock_entity
    data_source = DataStore(client=mock_datastore, project_id="foo")

    # act assert
    assert data_source.get_tm_release_date(questionnaire) == {
        "tmreleasedate": tm_release_date.isoformat()
    }
    mock_datastore.get.assert_called_once_with(
        Key("TmReleaseDate", questionnaire.upper(), project="foo")
    )


def test_delete_questionnaire_tm_release_date_with_valid_fields(
    mock_datastore, questionnaire, tm_release_date
):
    mocked_key = mock.MagicMock(name=questionnaire.upper())
    mock_entity = datastore.Entity(key=mocked_key)
    mock_entity["questionnaire"] = questionnaire.upper()
    mock_entity["tmreleasedate"] = tm_release_date
    mock_datastore.get.return_value = mock_entity
    data_source = DataStore(client=mock_datastore, project_id="foo")

    data_source.delete_tm_release_date(questionnaire)
    mock_datastore.delete.assert_called_once_with(mock_entity)
