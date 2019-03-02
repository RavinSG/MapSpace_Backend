from dbCon import db, timezone
from datetime import datetime
from bson.codec_options import CodecOptions

land_value = db.landValue.with_options(codec_options=CodecOptions(tz_aware=True, tzinfo=timezone))


def add_land_value(location, value, admin):
    currentDT = datetime.utcnow()
    land = land_value.find_one({"location": location})
    if land is None:
        post_data = {
            'location': location,
            'value': value,
            'updated_by': admin,
            'history': [[currentDT, value]],
            'last_updated': currentDT
        }
        result = land_value.insert_one(post_data)
        print('One post: {0}'.format(result.inserted_id))
    else:
        update_land_value(location, value, admin)


def update_land_value(location, value, admin):
    currentDT = datetime.utcnow()
    land_value.update_one(
        {"location": location},
        {"$set": {"value": value,
                  "last_updated": currentDT,
                  "updated_by": admin},
         "$push": {"history": [currentDT, value]}
         },
    )


def get_land_value(location, history=False):
    land = land_value.find_one({"location": location})
    if (history):
        return land['history']
    else:
        return land["value"]


# add_land_value("colombo", 1000000, "SK")
# update_land_value("colombo", 2000000, "bleh")
hist = get_land_value("colombo", history=False)
print(hist)
