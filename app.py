import sys
from flask import Flask
app = Flask(_name_)

@app.route("/")
def home():
    return f"Hello from Azure App Service! Python {sys.version}"
