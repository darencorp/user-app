from flask import Flask
from flask_cors import CORS

from src.v1.routes import api_v1

"""
This is main file. Here are defined things such as application server,
CORS policy and global routing between different versions of API.

"""

app = Flask(__name__)
cors = CORS(app, resources={'*': {'origins': '*'}})

app.register_blueprint(api_v1, url_prefix='/v1')


if __name__ == '__main__':
    app.run(debug=False, host='0.0.0.0', port=5000)
