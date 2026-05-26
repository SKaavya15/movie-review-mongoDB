from pymongo import MongoClient

client = MongoClient("mongodb://localhost:27017/")

db = client["movie_review"]

collection = db["movie"]

print("MongoDB Connected Successfully")

