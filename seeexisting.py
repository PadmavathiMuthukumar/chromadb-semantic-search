import chromadb
client = chromadb.PersistentClient()
collection =client.get_collection(name="vehicles")
print(collection.get())