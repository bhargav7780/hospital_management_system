from utils.db_connection import db
from bson.objectid import ObjectId
from datetime import datetime

appointments = db["appointments"]

def book_appointment(data):
    data["created_at"] = datetime.utcnow()
    return appointments.insert_one(data).inserted_id

def get_appointments():
    return list(appointments.find())
