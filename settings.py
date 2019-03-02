MONGO_HOST = 'localhost'
MONGO_PORT = 27017

MONGO_DBNAME = 'MapSpace'

RESOURCE_METHODS = ['GET', 'POST', 'DELETE']
ITEM_METHODS = ['GET', 'PATCH', 'PUT', 'DELETE']

user_schema = {
    'username': {
        'type': 'string',
        'minlength': 1,
        'maxlength': 10
    },
    'password': {
        'type': 'string',
        'minlength': 1,
        'maxlength': 10
    },
    'create_time': {
        'type': 'datetime'
    },
    'last_login': {
        'type': 'datetime'
    }
}

loginData = {
    'item_title': 'loginData',
    'additional_lookup': {
        'url': 'regex("[\w]+")',
        'field': 'username'
    },
    'resource_methods': ['GET', 'POST'],
    'schema': user_schema
}

DOMAIN = {
    'loginData': loginData
}
