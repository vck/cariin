from redisearch import Client, TextField

# Creating a client with a given index name
client = Client('myIndex')

# Creating the index definition and schema
client.create_index((TextField('title', weight=5.0), TextField('body')))

# Indexing a document
client.add_document('doc1', title = 'RediSearch', body = 'Redisearch impements a search engine on top of redis')

