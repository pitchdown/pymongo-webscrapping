import json
from pymongo import MongoClient


with open('data.json', 'r', encoding='utf-8') as f:     results = json.load(f)

# Connect to MongoDB
client = MongoClient('mongodb://localhost:27017/')
db = client['recipe_database']
collection = db['drinks_recipes']

# Insert scraped data
for result in results:
  collection.update_one({'recipe_url': result['recipe_url']}, {'$set': result}, upsert=True)


# Function to calculate the average number of ingredients
def average_ingredients():
    pipeline = [
        {"$project": {"ingredient_count": {"$size": "$ingredients"}}},
        {"$group": {"_id": None, "average_ingredients": {"$avg": "$ingredient_count"}}}
    ]
    result = list(collection.aggregate(pipeline))
    print(f"Average number of ingredients: {result[0]['average_ingredients']}")

# Function to calculate the average number of cooking stages
def average_cooking_stages():
    pipeline = [
        {"$project": {"instruction_count": {"$size": "$instructions"}}},
        {"$group": {"_id": None, "average_cooking_stages": {"$avg": "$instruction_count"}}}
    ]
    result = list(collection.aggregate(pipeline))
    print(f"Average number of cooking stages: {result[0]['average_cooking_stages']}")

# Function to find the recipe with the most ingredients
def recipe_with_most_ingredients():
    result = collection.find_one(sort=[("ingredients", -1)])
    print(f"Recipe with the most ingredients: {result['title']} (URL: {result['recipe_url']})")

# Function to find the author who posted the most recipes
def most_prolific_author():
    pipeline = [
        {"$group": {"_id": "$author", "recipe_count": {"$sum": 1}}},
        {"$sort": {"recipe_count": -1}},
        {"$limit": 1}
    ]
    result = list(collection.aggregate(pipeline))
    print(f"Author with the most recipes: {result[0]['_id']} ({result[0]['recipe_count']} recipes)")



# Running the statistics
average_ingredients()
average_cooking_stages()
recipe_with_most_ingredients()
most_prolific_author()
