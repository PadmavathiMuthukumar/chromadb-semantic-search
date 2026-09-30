import chromadb

# like remote controller which manages all the date
client=chromadb.PersistentClient() 

 # same like a table in SQL
collection = client.get_or_create_collection(name="vehicles")

print("Collection Created:", collection.name)

# add date to this collection with meta data
collection.add(
documents=[
"Bus carries passengers on road",
"Plane flies across countries",
"Boat travels on water",
"Bicycle runs without fuel"
],
ids=["bus1", "plane1", "boat1", "bike1"],
metadatas=[
    {
        "type":"public_transport",
        "fuel":"diesel"
    },
    {
        "type":"air_transport",
        "fuel":"jet"
    },
    {
            "type":"water_transport",
            "fuel":"diesel"
    },
    {
            "type":"personal_transport",
            "fuel":"manual"
    }
]
)

#print the result
print("data and metadata is added successfully")

vehi=client.get_collection("vehicles")
#to vieew the metadata
data=vehi.get(include=["documents","metadatas"])

print("All documents with metadata")
for i,doc,meta in zip(data["ids"],data["documents"],data["metadatas"]):
    print(f"{i} -> {doc} | Metadata: {meta}")

#filter by transport type
public_transport =collection.get(where= {"type":"personal_transport" })
print("Personal Transport:")
print(public_transport)