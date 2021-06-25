from api import api, init_datastore
from google.cloud import datastore

datastore_client = datastore.Client()

init_datastore(api, datastore_client)

if __name__ == "__main__":
    api.run(host="0.0.0.0", port=5011, debug=True)
