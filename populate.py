from redisearch import Client, TextField
import json

UNIQ = "db.txt"
# Creating a client with a given index name
client = Client('myIndex')

docs = []

with open(UNIQ) as corpus:
    # Indexing a document
    for row in corpus:
        corp = json.loads(row)
        if corp["url_id"] in docs:
            continue
        doc_id = corp["url_id"]
        print(f"adding document id {doc_id}")
        try:
            client.add_document(corp["url_id"], title = corp["title"], body=corp["url"])
        except Exception:
            continue
        docs.append(corp["url_id"])
