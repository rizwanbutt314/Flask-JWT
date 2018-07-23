from flask_restful import Resource, reqparse
from flask import jsonify, make_response
from flask_jwt_extended import create_access_token

import copy

from common.constants import API_PARAMS, USERS
from common.utils import parse_request_arguments


class GetAPIToken(Resource):
    def get(self):
        response = dict()
        status = 200

        request_data = parse_request_arguments(API_PARAMS)
        user = request_data['user']

        #If no user value given
        if not user:
            response = {
                'msg': 'User Missing'
            }
            status = 400
        #If user exists
        elif request_data['user'] in USERS:
            access_token = create_access_token(identity=request_data['user'])
            response = {
                'access_token': access_token
            }
        #Invalid user
        else:
            response = {
                'msg': 'Invalid User'
            }
            status = 404

        return make_response(jsonify(response), status)
