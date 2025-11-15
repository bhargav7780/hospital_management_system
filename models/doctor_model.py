from utils.db_connection import db
from bson.objectid import ObjectId

doctors = db["doctors"]

def add_doctor(data):
    return doctors.insert_one(data).inserted_id

def get_all_doctors():
    return list(doctors.find())
