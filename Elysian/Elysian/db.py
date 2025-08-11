import os
from mongoengine import connect

# MongoDB connection URI
MONGO_URI = os.getenv(
    "MONGO_URI",
    "mongodb+srv://ajay:bGptBVJS5Cem3pek@cluster0.lkwz9i8.mongodb.net/mydb"
)

# Connect to MongoDB
connect(host=MONGO_URI)
