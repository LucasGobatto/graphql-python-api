from flask import Flask
from flask_cors import CORS

app = Flask(__name__)
CORS(app)

@app.route('/')
def hello():
  return '<a href="http://localhost:5000/graphql">Graphql playground</a>'

