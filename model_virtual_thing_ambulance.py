import math
import random

from datetime import datetime
from description_gen import rand_description


# Function to Create Virtual Things
def create_random_virtual_thing(idVirtualThing):
    # description = rand_description(words, position, book)
    category = "Smart Health Services"
    identifier = 'Ambulance ' + str(idVirtualThing)
    alternate_name = 'Ambulance  '
    title = ''
    virtual_thing = {
        # 'id': idVirtualThing,
        'name': 'VTH' + title.ljust(7 - int(math.log10(idVirtualThing)), '0') + str(idVirtualThing),
        'base': '/api/virtualthings/',
        'name_friendly': alternate_name + str(idVirtualThing),
        'properties':
            {
                'description': "A vehicle equipped for taking sick or injured people to and from hospital, especially in emergencies.",
                'category': category,
                'latitude': random.uniform(37.14, 37.21),
                'longitude': random.uniform(-3.54, -3.63),
                'status': "Free",
            }
        ,
        'actions': {
            'admin': "Unknown",
            'description': "Transport a patient",
        },
        'events':
            {
                'creation': datetime.now(),
                'last_modified': datetime.now(),
            },
    }
    return virtual_thing
