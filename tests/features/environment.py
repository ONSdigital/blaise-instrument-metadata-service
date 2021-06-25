from api.api import api
from datetime import datetime
from typing import Dict

class MockDataStore():
    def __init__(self):
        self.store = {}

    def add_livedate(self, questionnaire: str, livedate: datetime) -> Dict[str, str]:
        self.store[questionnaire] = {"questionnaire": questionnaire, "livedate": livedate}
        return {questionnaire: livedate.isoformat()}

    def get_livedate(self, questionnaire: str):
        return {"livedate": self.store[questionnaire]["livedate"].isoformat()}

    def delete_livedate(self, questionnaire: str):
        if questionnaire in self.store:
            self.store.pop(questionnaire)


def before_scenario(context, _scenario):
    mock_datastore = MockDataStore()
    context.datastore = mock_datastore
    api.datastore = mock_datastore
    context.client = api.test_client()
