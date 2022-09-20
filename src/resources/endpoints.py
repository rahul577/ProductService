import sys
sys.path.append("..")
from controllers import Ingestion, User
from flask import Flask, request

app = Flask(__name__)

@app.route('/product', methods = ["GET", "POST"])
def index():
    ingestionInstance = Ingestion();
    if request.method == "POST":
        return ingestionInstance.addProduct()

    if request.method == "GET":
        return ingestionInstance.getProduct()

@app.route('/genre', methods = ["POST"])
def genre():
    userInstance = User();
    if request.method == "POST":
        return userInstance.addGenre()

@app.route('/provider', methods = ["POST"])
def provider():
    userInstance = User();
    if request.method == "POST":
        return userInstance.addProviderForProduct()

if __name__ == '__main__':
    app.run(debug=True)