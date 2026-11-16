from pymongo import MongoClient


mongo_uri = "mongodb+srv://@.gbgdopi.mongodb.net/?appName=julhetzenauer"

client = MongoClient(mongo_uri)


db = client.witze

test_data_collection = db.witze


user2 = [
    {'witz': input("schreibe deinen witz!") }]

test_data_collection.insert_many(user2)

l=(input("Alle Witze anzeigen?, Ja/Nein "))

if (l=="Ja"):
    for i in test_data_collection.find({}, {'_id': 0, 'witz': 1}):
        print(i['witz'])

# Close the MongoDB connection
client.close()
