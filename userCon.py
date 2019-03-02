from dbCon import db, timezone
from datetime import datetime
from bson.codec_options import CodecOptions

users = db.loginData.with_options(codec_options=CodecOptions(tz_aware=True, tzinfo=timezone))


def add_user(username, password):
    user = users.find_one({'username': username})
    if user is None:
        currentDT = datetime.utcnow()
        post_data = {
            'username': username,
            'password': password,
            'create_time': currentDT,
            'last_login': currentDT
        }
        result = users.insert_one(post_data)
        print('One post: {0}'.format(result.inserted_id))
    else:
        print('Username already taken')


def verify_user(username, password):
    user = users.find_one({'username': username})
    if user is not None:
        if user['password'] == password:
            return True
        else:
            return False
    else:
        return False


def login_user(username, password):
    if verify_user(username, password):
        currentDT = datetime.utcnow()
        users.update_one(
            {"username": username},
            {"$set": {"last_login": currentDT}}
        )


add_user("ravin", "test123")
login_user("ravin", "test123")
