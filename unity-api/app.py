import os
from flask import Flask
from flask_cors import CORS
from dotenv import load_dotenv
from routes.files import files_bp

app = Flask(__name__)
CORS(app)
load_dotenv()

app.register_blueprint(files_bp)

@app.route("/")
def hello_world():
    return "Unity Project Presentation API"

if __name__ == "__main__":
    app.run(debug=True, host='0.0.0.0', port=5001)
