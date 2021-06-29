from app.app import app
from datetime import datetime
from typing import Dict


class MockDataStore():
    def __init__(self):
        self.store = {}

    def add_livedate(self, questionnaire: str, livedate: datetime) -> Dict[str, str]:
        self.store[questionnaire] = {"questionnaire": questionnaire, "livedate": livedate}
        return {questionnaire: livedate.isoformat()}

    def get_livedate(self, questionnaire: str):
        if questionnaire not in self.store:
            return None
        return {"livedate": self.store[questionnaire]["livedate"].isoformat()}

    def delete_livedate(self, questionnaire: str):
        if questionnaire in self.store:
            self.store.pop(questionnaire)
        return {"deleted": f"{questionnaire}"}


def before_scenario(context, _scenario):
    mock_datastore = MockDataStore()
    context.datastore = mock_datastore
    app.datastore = mock_datastore
    context.client = app.test_client()
