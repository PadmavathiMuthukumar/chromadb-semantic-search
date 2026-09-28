import chromadb

# like remote controller which manages all the date
client=chromadb.Client() 

 # same like a table in SQL
collection = client.create_collection(name="vehicles")

print("Collection Created:", collection.name)

# add date to this collection
collection.add(
    documents=[
        "Car runs on land", #encode into embeddings automatically
        "Plane flies in the sky",
        "Boat travels on water",
        "Bus is public transport on road"
    ],
    ids=[
        "car1", "plane1","boat1","bus1"
    ]
)

#Query the collection
results=collection.query(
    query_texts=["if i have to catch fish, what should i use"],
    n_results=2
)
#print the result
print(results)
