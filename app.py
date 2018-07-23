from flask import Flask, request
from flask_cors import CORS
from flask_restful import Resource, Api

from views.view_zipcode import ZipCode
from views.view_county import County
from views.view_state import State
from views.view_msa import Msa
from views.view_state_list import StateList
from views.view_msa_list import MsaList
from views.view_county_list import CountyList

app = Flask(__name__)
CORS(app)
api = Api(app)

# Routes
api.add_resource(ZipCode, '/zipcode', endpoint="zipcode")
api.add_resource(County, '/county', endpoint="county")
api.add_resource(State, '/state', endpoint="state")
api.add_resource(Msa, '/msa', endpoint="msa")
api.add_resource(StateList, '/get_state', endpoint="get_state")
api.add_resource(MsaList, '/get_msa', endpoint="get_msa")
api.add_resource(CountyList, '/get_county', endpoint="get_county")

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=9000, debug=True)
