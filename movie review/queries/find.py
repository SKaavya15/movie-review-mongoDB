from pymongo import MongoClient
import json

# Connect MongoDB
client = MongoClient("mongodb://localhost:27017/")

print("MongoDB Connected Successfully")

# Create Database
db = client["movie_review_db"]

# Create Collection
collection = db["movies"]
with open("data.json", "r") as file:
    movies_data = json.load(file)

# Insert JSON Data
collection.insert_many(movies_data)

print("JSON Data Inserted Successfully")

movie = collection.find_one(
    {"title": "Inception"}
)

print(movie)

movie = collection.find_one(
    {"title": "Inception"}
)

print(movie)

for movie in collection.find(
    {"genre": "Action"}
):
    print(movie)
for movie in collection.find(
    {"rating": {"$gt": 8.5}}
):
    print(movie)