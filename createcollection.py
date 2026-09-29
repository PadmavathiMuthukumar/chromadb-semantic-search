import chromadb

# like remote controller which manages all the date
client=chromadb.PersistentClient() 

 # same like a table in SQL
collection = client.create_collection(name="vehicles")

print("Collection Created:", collection.name)

# add date to this collection
collection.add(
    documents=[
        "Car runs on land" #encode into embeddings automatically
    ],
    ids=[
        "car1"
    ]
)

print("data added")