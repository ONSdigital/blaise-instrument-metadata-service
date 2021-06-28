import os
from google.cloud import datastore

from app import init_datastore, app

project_id = os.getenv("PROJECT_ID", "ons-blaise-v2-dev-ali-9")

datastore_client = datastore.Client()

init_datastore(app, datastore_client, project_id)

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5011)
