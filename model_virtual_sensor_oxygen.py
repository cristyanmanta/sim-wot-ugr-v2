import math
import random

from datetime import datetime
from description_gen import rand_description


# Function to Create Virtual Sensors
def create_random_virtual_sensor(idVirtualSensor):
    category = "Smart Sensing Services"
    identifier = 'Oxygen Sensor ' + str(idVirtualSensor)
    alternate_name = 'Oxygen Sensor '
    title = ''
    virtual_sensor = {
        # 'id': idVirtualSensor,
        'name': 'VSN' + title.ljust(7 - int(math.log10(idVirtualSensor)), '0') + str(idVirtualSensor),
        'base': '/api/virtualsensors/',
        'name_friendly': alternate_name + str(idVirtualSensor),
        'properties':
            {
                'description': "Also known as the O2 sensor because O2 is the chemical formula for oxygen, the oxygen "
                               "sensor monitors how much oxygen is present in the system. ",
                'category': category,
                'latitude': random.uniform(37.14, 37.21),
                'longitude': random.uniform(-3.54, -3.63),
                'status': "Operating ",
            }
        ,
        'actions': {
            'admin': "Unknown",
            'description': "Sense O2 level",
        },
        'events':
            {
                'creation': datetime.now(),
                'last_modified': datetime.now(),
            },
    }
    return virtual_sensor
