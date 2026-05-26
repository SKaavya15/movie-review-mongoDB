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

#finds highest movie rating

print("finds highest movie rating------------------------")
highest = collection.find().sort(
    "rating", -1
).limit(1)

for movie in highest:
    print(movie)

#lowest movie rating
print("lowest movie rating")

lowest = collection.find().sort(
    "rating", 1
).limit(1)

for movie in lowest:
    print(movie)

#movies released after 2015
print("movies released after 2015-------------------------")
for movie in collection.find(
    {"release_year": {"$gt": 2015}}
):
    print(movie)

#count movies by genres
print("count movies by genres----------------------------")

pipeline = [
{
    "$group":
    {
        "_id": "$genre",
        "total_movies":
        {"$sum": 1}
    }
}
]

for result in collection.aggregate(pipeline):
    print(result)

#Average Rating by Genre
print("Average Rating by Genre---------------------------------------")
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
#Total Number of Movies
print("Total Number of Movies-------------------------------")
count = collection.count_documents({})

print("Total Movies:", count)
#Find Movies with Rating Greater Than 8.5

print("Find Movies with Rating Greater Than 8.5-----------------------------")
for movie in collection.find(
    {"rating": {"$gt": 8.5}}
):
    print(movie)
#Sort Movies by Rating
print("Sort Movies by Rating")
for movie in collection.find().sort(
    "rating", -1
):
    print(movie)
#Find Movies by Genre
print("Find Movies by Genre-----------------------------------")
for movie in collection.find(
    {"genre": "Action"}
):
    print(movie)
#Reviewer-wise Movie Count
print("Reviewer-wise Movie Count------------------------------------")
pipeline = [
{
    "$group":
    {
        "_id": "$reviewer",
        "movies_reviewed":
        {"$sum": 1}
    }
}
]

for result in collection.aggregate(pipeline):
    print(result)