from utils.db_connection import db
from bson.objectid import ObjectId

patients = db["patients"]

def add_patient(data):
    return patients.insert_one(data).inserted_id

def get_all_patients():
    return list(patients.find())

def get_patient(pid):
    return patients.find_one({"_id": ObjectId(pid)})

def delete_patient(pid):
    return patients.delete_one({"_id": ObjectId(pid)})
