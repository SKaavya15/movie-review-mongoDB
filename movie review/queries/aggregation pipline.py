from pymongo import MongoClient
import json

# Connect MongoDB
client = MongoClient("mongodb://localhost:27017/")

print("MongoDB Connected Successfully")

# Create Database
db = client["movie_review_db"]

# Create Collection
collection = db["movies"]

# Open JSON File
with open("data.json", "r") as file:
    movies_data = json.load(file)

pipeline = [
{
    "$group":
    {
        "_id": "$genre",
        "average_rating":
        {
            "$avg": "$rating"
        }
    }
}
]

for result in collection.aggregate(pipeline):
    print(result)
collection.drop()

print("Collection Deleted")