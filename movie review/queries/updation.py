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

# Insert JSON Data
collection.insert_many(movies_data)

print("JSON Data Inserted Successfully")

collection.update_one(
    {"title": "Titanic"},
    {
        "$set":
        {
            "rating": 8.5
        }
    }
)

print("One Document Updated")

collection.update_many(
    {"genre": "Sci-Fi"},
    {
        "$set":
        {
            "reviewer": "Admin"
        }
    }
)

print("Multiple Documents Updated")