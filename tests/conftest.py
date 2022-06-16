import pytest
import datetime
from unittest import mock


@pytest.fixture
def questionnaire():
    return "foobar"


@pytest.fixture
def to_start_date():
    return datetime.date(2021, 1, 1)


@pytest.fixture
def tm_release_date():
    return datetime.date(2021, 1, 1)


@pytest.fixture
def mock_datastore():
    return mock.MagicMock()


@pytest.fixture
def current_url():
    return "http://localhost"
