from datetime import datetime

from google.cloud import datastore
from google.cloud.datastore import Key

LIVE_DATE_KIND = "LiveDate"


class DataStore:
    def __init__(self, client: datastore.Client, project_id: str):
        self.client = client
        self.project_id = project_id

    def add_livedate(self, questionnaire: str, livedate: datetime):
        questionnaire = questionnaire.upper()
        # The Cloud Datastore key for the new entity
        task_key = self.client.key(LIVE_DATE_KIND, questionnaire)

        # Prepares the new entity
        task = datastore.Entity(key=task_key)
        task["questionnaire"] = questionnaire
        task["livedate"] = livedate

        # Saves the entity
        self.client.put(task)
        return {questionnaire: task['livedate'].isoformat()}

    def get_livedate(self, questionnaire: str):
        questionnaire = questionnaire.upper()
        # Retrieves the key by the name/id of the kind
        result = self.client.get(Key(LIVE_DATE_KIND, questionnaire, project=self.project_id))
        if result is None:
            return None
        print(f"result = {result}")
        return {"livedate": result["livedate"].isoformat()}

    def delete_livedate(self, questionnaire: str):
        questionnaire = questionnaire.upper()
        result = self.client.get(Key(LIVE_DATE_KIND, questionnaire, project=self.project_id))
        self.client.delete(result)

        print(f"Deleted {result}")
