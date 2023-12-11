from datetime import datetime

from google.cloud import datastore
from google.cloud.datastore import Key

TO_START_DATE_KIND = "ToStartDate"
TM_RELEASE_DATE_KIND = "TmReleaseDate"


class DataStore:
    def __init__(self, client: datastore.Client, project_id: str):
        self.client = client
        self.project_id = project_id

    def add_to_start_date(self, questionnaire: str, to_start_date: datetime):
        questionnaire = questionnaire.upper()
        # The Cloud Datastore key for the new entity
        task_key = self.client.key(TO_START_DATE_KIND, questionnaire)

        # Prepares the new entity
        task = datastore.Entity(key=task_key)
        task["questionnaire"] = questionnaire
        task["tostartdate"] = to_start_date

        # Saves the entity
        self.client.put(task)
        return {questionnaire: task["tostartdate"].isoformat()}

    def get_to_start_date(self, questionnaire: str):
        questionnaire = questionnaire.upper()
        # Retrieves the key by the name/id of the kind
        result = self.client.get(
            Key(TO_START_DATE_KIND, questionnaire, project=self.project_id)
        )
        if result is None:
            return None
        print(f"result = {result}")
        return {"tostartdate": result["tostartdate"].isoformat()}

    def delete_to_start_date(self, questionnaire: str):
        questionnaire = questionnaire.upper()
        result = self.client.get(
            Key(TO_START_DATE_KIND, questionnaire, project=self.project_id)
        )
        self.client.delete(result)

        print(f"Deleted {result}")

    def add_tm_release_date(self, questionnaire: str, tm_release_date: datetime):
        questionnaire = questionnaire.upper()
        # The Cloud Datastore key for the new entity
        task_key = self.client.key(TM_RELEASE_DATE_KIND, questionnaire)

        # Prepares the new entity
        task = datastore.Entity(key=task_key)
        task["questionnaire"] = questionnaire
        task["tmreleasedate"] = tm_release_date

        # Saves the entity
        self.client.put(task)
        return {questionnaire: task["tmreleasedate"].isoformat()}

    def get_tm_release_date(self, questionnaire: str):
        questionnaire = questionnaire.upper()
        # Retrieves the key by the name/id of the kind
        result = self.client.get(
            Key(TM_RELEASE_DATE_KIND, questionnaire, project=self.project_id)
        )
        if result is None:
            return None
        print(f"result = {result}")
        return {"tmreleasedate": result["tmreleasedate"].isoformat()}

    def delete_tm_release_date(self, questionnaire: str):
        questionnaire = questionnaire.upper()
        result = self.client.get(
            Key(TM_RELEASE_DATE_KIND, questionnaire, project=self.project_id)
        )
        self.client.delete(result)

        print(f"Deleted {result}")
