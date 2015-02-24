from syncano import client
import pickle
import os
SyncanoApi = client.SyncanoApi
instance_name = os.environ.get("SYNCANO_INSTANCE_NAME")
api_key = os.environ.get("SYNCANO_API_KEY")
vals = {}
syncano = SyncanoApi(instance_name,api_key)

project = syncano.project_new('wedding_registry', message_id=1)
vals['project_id'] = project['data']['project']['id']
collection_key = "14578"
collection_name = "default"
folder_name = "fuzzy"
syncano.collection_new(vals["project_id"],collection_name,collection_key)
syncano.folder_new(vals["project_id"],folder_name,collection_key=collection_key)


vals["collection_id"] = syncano.collection_get_one(vals["project_id"],collection_key=collection_key)
vals["folder_id"] = syncano.folder_get_one(vals["project_id"],folder_name,collection_key=collection_key)

print vals
