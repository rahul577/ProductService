from flask import Flask
from controllers.ingestion import Ingestion

app = Flask(__name__)

@app.route('/')
def index():
    return Ingestion.update()

if __name__ == '__main__':
    app.run(debug=True)