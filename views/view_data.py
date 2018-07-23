from flask_restful import Resource, reqparse
from flask import jsonify, make_response
from flask_jwt_extended import jwt_required, get_jwt_identity, fresh_jwt_required

import copy

from common.constants import API_PARAMS, USERS
from common.utils import parse_request_arguments


class GetData(Resource):
    @jwt_required
    def get(self):
        response = dict()
        status = 200

        request_data = parse_request_arguments(API_PARAMS)
        current_user = get_jwt_identity()

        response['user'] = current_user

        return make_response(jsonify(response), status)
