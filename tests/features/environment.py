from datetime import datetime
from typing import Dict

from app.app import app


class MockDataStore:
    def __init__(self):
        self.store = {}

    def add_to_start_date(
        self, questionnaire: str, to_start_date: datetime
    ) -> Dict[str, str]:
        self.store[questionnaire] = {
            "questionnaire": questionnaire,
            "tostartdate": to_start_date,
        }
        return {questionnaire: to_start_date.isoformat()}

    def get_to_start_date(self, questionnaire: str):
        if questionnaire not in self.store:
            return None
        return {"tostartdate": self.store[questionnaire]["tostartdate"].isoformat()}

    def delete_to_start_date(self, questionnaire: str):
        if questionnaire in self.store:
            self.store.pop(questionnaire)
        return {"deleted": f"{questionnaire}"}

    def add_tm_release_date(
        self, questionnaire: str, tm_release_date: datetime
    ) -> Dict[str, str]:
        self.store[questionnaire] = {
            "questionnaire": questionnaire,
            "tmreleasedate": tm_release_date,
        }
        return {questionnaire: tm_release_date.isoformat()}

    def get_tm_release_date(self, questionnaire: str):
        if questionnaire not in self.store:
            return None
        return {"tmreleasedate": self.store[questionnaire]["tmreleasedate"].isoformat()}

    def delete_tm_release_date(self, questionnaire: str):
        if questionnaire in self.store:
            self.store.pop(questionnaire)
        return {"deleted": f"{questionnaire}"}


def before_scenario(context, _scenario):
    mock_datastore = MockDataStore()
    context.datastore = mock_datastore
    app.datastore = mock_datastore
    context.client = app.test_client()
