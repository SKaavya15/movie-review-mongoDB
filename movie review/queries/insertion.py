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




movie = {
    "movie_id": 11,
    "title": "Avatar",
    "genre": "Sci-Fi",
    "release_year": 2009,
    "rating": 8.4,
    "review": "Visual masterpiece",
    "reviewer": "Karthik"
}

collection.insert_one(movie)

print("One Document Inserted")