from pymongo import MongoClient
import json


client = MongoClient("mongodb://localhost:27017/")

print("MongoDB Connected Successfully")


db = client["movie_review_db"]


collection = db["movies"]


with open("data.json", "r") as file:
    movies_data = json.load(file)


collection.insert_many(movies_data)

for movie in collection.find().sort(
    "rating", -1):
    print(movie)
for movie in collection.find().limit(5):
    print(movie)