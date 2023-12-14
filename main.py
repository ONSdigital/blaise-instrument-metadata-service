import os

from google.cloud import datastore

from app import app, init_datastore

project_id = os.getenv("PROJECT_ID", default="default_project_id")

datastore_client = datastore.Client()

init_datastore(app, datastore_client, project_id)

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5011)
