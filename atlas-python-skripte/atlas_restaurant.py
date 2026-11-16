from operator import gt, lt

from pymongo import MongoClient

# MongoDB connection string
connection_string = "mongodb+srv://:testgerhard.0rechap.mongodb.net/"  # Example: "mongodb+srv://<username>:<password>@cluster0.mongodb.net/?retryWrites=true&w=majority"

# Connect to MongoDB
client = MongoClient(connection_string)

# database name
db = client['sample_restaurant']

# collection name
collection = db['restaurant']

# Query to retrieve all documents
movieCollection = db['movies']
userCollection = db['users']
embeddedMoviesCollection = db['embedded_movies']
first5movies = movieCollection.find().limit(5)
short_movies = movieCollection.find(    {'genres' : 'Short'})
users = userCollection.find()
englishEmbeddedMovies = embeddedMoviesCollection.find(    {'languages' : 'English'})


# Print all the documents in the collection
for r in first5movies:
    print(r)

# Close the connection
client.close()
