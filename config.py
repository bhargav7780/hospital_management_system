import os

# Example local MongoDB (change to your Atlas URI if needed)
MONGO_URI = os.getenv("MONGO_URI", "mongodb+srv://bhargav:7igyqhbDUrvmm0oc@cluster0.hl68t5o.mongodb.net/hospital_db?retryWrites=true&w=majority")
SECRET_KEY = os.getenv("SECRET_KEY", "76d3ffaee701c12efc8a62ef6df7100f")
