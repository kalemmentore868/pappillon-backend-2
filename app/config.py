from flask import Flask
from flask_pymongo import PyMongo
from flask_cors import CORS

app = Flask(__name__)
CORS(app, origins="*")

  # Allow all origins and methods
# app.config["SECRET_KEY"] = "fbf78234a78cc1a9f90e64e2d134dbfb850641bf"
app.config["MONGO_URI"] = "mongodb+srv://kalemmentore868:5oKmd0wWf5kEF3no@cluster0.p622hsk.mongodb.net/dev?retryWrites=true&w=majority&tlsAllowInvalidCertificates=true"

# Set up MongoDB
mongo = PyMongo(app)

