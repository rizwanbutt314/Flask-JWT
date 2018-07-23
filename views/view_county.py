from flask_restful import Resource, reqparse
from flask import jsonify, make_response

import copy
import decimal



class County(Resource):

    def get(self):
        request_data = parse_request_arguments(COUNTY_PARAMS)
        search_params = copy.copy(request_data)

        return make_response(jsonify({
            "data": result,
            "total_count": int(query_count[0][0]),
            "total_households": int(query_count[0][1]) if query_count[0][1] else 0,
            "households_percent": float(households_percent),
        }), 200)
