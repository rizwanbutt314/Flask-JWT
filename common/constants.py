DATABASE_URI = "postgres://eatclpvgvasmes:36a0e018a451ecc46db00e8b9fe8c7e006b442c2ec1143adcd9a0e7bdbe43370@ec2-23-21-217-27.compute-1.amazonaws.com:5432/dde9jrg934jkgl"

#ZipCode View Params list
ZIPCODE_PARAMS = [
    'group',
    'state',
    'msa',
    'county',
    'limit',
    'offset',
]

#County View Params list
COUNTY_PARAMS = [
    'group',
    'state',
    'msa',
    'limit',
    'offset',
]

#State View Params list
STATE_PARAMS = [
    'group',
    'limit',
    'offset',
]

#Msa View Params list
MSA_PARAMS = [
    'group',
    'limit',
    'offset',
]

#Swagger Params Object
SWAGGER_PARAMS = {
    'limit':{
        "name": "limit",
        "description": "Limiting the length of JSON data",
        "required": False,
        "dataType": "integer",
        "paramType": "query"
    },
    'offset':{
        "name": "offset",
        "description": "Starting number of database row",
        "required": False,
        "dataType": "integer",
        "paramType": "query"
    },
    'group':{
        "name": "group",
        "description": "Search by group name (multiple values separated by comma)",
        "required": False,
        "dataType": "string",
        "paramType": "query"
    },
    'state':{
        "name": "state",
        "description": "Search by state name",
        "required": False,
        "dataType": "string",
        "paramType": "query"
    },
    'msa':{
        "name": "msa",
        "description": "Search by msa name",
        "required": False,
        "dataType": "string",
        "paramType": "query"
    },
    'county':{
        "name": "county",
        "description": "Search by county name",
        "required": False,
        "dataType": "string",
        "paramType": "query"
    },
    'error':{
        "code": 500,
        "message": "Error while running SQL query"
    }
}
