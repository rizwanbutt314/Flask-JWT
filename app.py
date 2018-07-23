from flask import Flask, request
from flask_cors import CORS
from flask_restful import Resource, Api
from flask_jwt_extended import JWTManager

from views.view_auth import GetAPIToken
from views.view_data import GetData
from common.constants import SECRET_KEY

from datetime import timedelta

app = Flask(__name__)

# Setup the Flask-JWT-Extended extension
app.config['JWT_SECRET_KEY'] = SECRET_KEY
# Token Expires after 1 hour
_seconds = 1 * 3600
app.config['JWT_ACCESS_TOKEN_EXPIRES'] = timedelta(seconds=_seconds)
jwt = JWTManager(app)

CORS(app)
api = Api(app)

# Routes
api.add_resource(GetAPIToken, '/get_token', endpoint="get-api-token")
api.add_resource(GetData, '/data', endpoint="get-sample-data")

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=9000, debug=True)
