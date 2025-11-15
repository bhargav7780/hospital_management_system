from utils.db_connection import db
from bson.objectid import ObjectId

users = db["users"]

def create_user(username, password_hash, role="receptionist"):
    doc = {"username": username, "password": password_hash, "role": role}
    return users.insert_one(doc).inserted_id

def find_by_username(username):
    return users.find_one({"username": username})

def find_by_id(uid):
    return users.find_one({"_id": ObjectId(uid)})
