from dbCon import db, timezone
from datetime import datetime
from bson.codec_options import CodecOptions

users = db.userData.with_options(codec_options=CodecOptions(tz_aware=True, tzinfo=timezone))


def add_saved_land(area, points, center):
    currentDT = datetime.utcnow()
    land_item = {
        'area': area,
        'points': points,
        'center': center,
        'time': currentDT
    }
    users.find_one_and_update({'username': 'Ravin'},
                              {'$push':
                                   {'land_items': land_item}
                               }
                              )

