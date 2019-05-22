from dbCon import db, timezone
from datetime import datetime
from bson.codec_options import CodecOptions

land_value = db.landValue.with_options(codec_options=CodecOptions(tz_aware=True, tzinfo=timezone))


def add_land_value(location, city, price, id):
    currentDT = datetime.utcnow()
    land = land_value.find_one({"location": location})
    if land is None:
        post_data = {
            'land_area': location,
            'city': city,
            'price': price,
            'id': id,
            'description': 'Purchase a land for your dream home from urban and sub urban areas of Ambewela City. '
                           'Lands starting from 170,000 LKR onwards'
        }
        result = land_value.insert_one(post_data)
        print('One post: {0}'.format(result.inserted_id))
    else:
        update_land_value(location, city, price)


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
    land = land_value.find_one({"city": location})
    if (history):
        return land['history']
    else:
        return land


def get_all_values(city=None):
    if city is not None:
        cursor = land_value.find({'city': city})
    else:
        cursor = land_value.find({})

    lands = []
    for doc in cursor:
        land = {
            'Land_Area': doc['land_area'],
            'City': doc['city'],
            'Price': doc['price'],
            'ID': doc['id'],
            'description': 'Purchase a land for your dream home from urban and sub urban areas of Ambewela City. '
                           'Lands starting from 170,000 LKR onwards',
            'src': doc['src'],
            'coords': doc['coords']
        }
        lands.append(land)

    return lands

# add_land_value('Embilipitiya City', 'Ratnapura', 25000, 5)
# add_land_value('Kandy City', 'Kandy ', 80000, 6)
# add_land_value('Biyagama', 'Gampaha', 260000, 7)
