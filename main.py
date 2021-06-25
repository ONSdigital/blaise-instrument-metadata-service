import os

from api import api, init_datastore
from google.cloud import datastore

project_id = os.getenv("project_id", "ons-blaise-v2-dev-nik12")

datastore_client = datastore.Client()

init_datastore(api, datastore_client, project_id)

if __name__ == "__main__":
    api.run(host="0.0.0.0", port=5011, debug=True)
