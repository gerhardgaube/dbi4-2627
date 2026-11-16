
from pymongo import MongoClient

# Replace the placeholders with your actual MongoDB connection string
mongo_uri = "mongodb+srv://gerhardgaube:test12345@testgerhard.0rechap.mongodb.net/"

# Connect to the MongoDB database
client = MongoClient(mongo_uri)

# Replace 'your_database_name' with your actual MongoDB database name
db = client.aiit33

# Create a collection named 'test_data'
test_data_collection = db.userdatenbank33

# Insert test data
user2 = [
    {'name': 'Alice', 'age': 25},
    {'name': 'Bob', 'age': 30},
    {'name': 'Charlie', 'age': 22},
    {'name': 'Gustav', 'age': 222}]




test_data_collection = db.userdatenbank33

# Insert test data
user3 = [
    {'name': 'Alice', 'age': 25},
 ]

test_data_collection.insert_many(user2)

# Close the MongoDB connection
client.close()
