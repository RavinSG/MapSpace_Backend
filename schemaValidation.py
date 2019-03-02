from cerberus import Validator

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
        'type': 'string'
    },
    'last_login': {
        'type': 'string'
    }
}

v = Validator(user_schema)
document = {"username": "ravin",
            "password": "test123",
            "create_time": "2019-03-02T05:16:52.237Z",
            "last_login": "2019-03-02T05:23:22.359Z"}

print(v.validate(document))