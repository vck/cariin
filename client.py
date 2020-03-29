from redisearch import Client, TextField

client = Client('myIndex')
while True:
    query = input("query > ")
    if query:
        q = client.search(query)
        n_match = len(q.docs)
        print(f"found match {n_match} for keyword {query}")
        for row in q.docs:
            print(row.id, row.title, row.body)

