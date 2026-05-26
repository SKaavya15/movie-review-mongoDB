MongoDB Movie Review Database Project
Project Description

The MongoDB Movie Review Database Project is a NoSQL database application developed using MongoDB and Python. The project stores movie details, genres, ratings, reviews, and reviewer information using collections and documents. It demonstrates CRUD operations, query operators, aggregation pipelines, and Python integration using the pymongo library.

Technologies Used
MongoDB
MongoDB Compass
Python
pymongo library
Visual Studio Code
Database Details
Database Name
movie_review_db
Collection Name
movies
Features
Stores movie reviews and ratings
Uses MongoDB collections and documents
Performs CRUD operations
Supports query filtering and aggregation
Integrates Python with MongoDB using pymongo
Handles unstructured movie data efficiently
Collection Structure

Each document contains:

Movie ID
Movie Title
Genre
Release Year
Rating
Review
Reviewer Name
Sample Document
{
    "movie_id": 1,
    "title": "Inception",
    "genre": "Sci-Fi",
    "release_year": 2010,
    "rating": 9.0,
    "review": "Excellent science fiction movie",
    "reviewer": "Arun"
}
Python Connection
from pymongo import MongoClient

client = MongoClient(
    "mongodb://localhost:27017/"
)

db = client["movie_review_db"]

collection = db["movies"]

print("MongoDB Connected Successfully")
CRUD Operations
Create
collection.insert_one({
    "movie_id": 11,
    "title": "Avatar",
    "genre": "Sci-Fi",
    "rating": 8.4
})
Read
for movie in collection.find():
    print(movie)
Update
collection.update_one(
    {"title": "Titanic"},
    {"$set": {"rating": 8.5}}
)
Delete
collection.delete_one(
    {"title": "Doctor Strange"}
)
Query Operations
Find Movies with Rating Greater Than 8.5
for movie in collection.find(
    {"rating": {"$gt": 8.5}}
):
    print(movie)
Find Movies by Genre
for movie in collection.find(
    {"genre": "Action"}
):
    print(movie)
Aggregation Pipeline
Average Rating by Genre
pipeline = [
{
    "$group":
    {
        "_id": "$genre",
        "average_rating":
        {"$avg": "$rating"}
    }
}
]

for result in collection.aggregate(pipeline):
    print(result)
Business Insights
Sci-Fi and Action movies have higher average ratings.
Highly rated movies are more popular among users.
Genre analysis helps identify audience preferences.
Aggregation queries help generate analytical reports.
MongoDB efficiently handles document-based movie data.
Ratings and reviews improve recommendation systems
