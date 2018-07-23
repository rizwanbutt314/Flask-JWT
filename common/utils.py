from flask_restful import reqparse


def map_request_params(params_list):
    parser = reqparse.RequestParser()
    for param in params_list:
        parser.add_argument(param)

    return parser.parse_args()


def parse_request_arguments(view_params):
    parsed_params = map_request_params(view_params)
    return parsed_params
