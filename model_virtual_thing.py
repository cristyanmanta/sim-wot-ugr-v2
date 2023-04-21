import math
import random
import xml.etree.ElementTree as ET

from datetime import datetime
from xml.etree import ElementTree
from xml.dom import minidom
from random import choice
from description_gen import rand_description

# Settings for Random Descriptions in vThings XML Documents

words = random.randint(50, 100)
position = random.randint(100, 500)
book = random.randint(1, 200)


def prettify(elem):
    """Return a pretty-printed XML string for the Element.
    """
    rough_string = ElementTree.tostring(elem, 'utf-8')
    reparsed = minidom.parseString(rough_string)
    return reparsed.toprettyxml(indent="  ")


# Pre-Data to Create Virtual Things

pre_virtual_things = [
    {
        'name': 'bicycle',
        'keyword': 'Bike, Bicycle',
        'categories': ['Private', 'Public transportation'],
        'action_name': 'To be ridden',
        'state': 'connected',
        'virtual_sensors': [
            {
                'name': 'Magnetic switch sensor',
                'classifier': 'Magnetic Sensor',
                'density_function': 1,
                'measure': 'Bike availability',
                'observed_property': 'Bike presence on slot',
                'min_value': 0,
                'max_value': 1,
                'sampling_time': 1
            }

        ]
    },
    {
        'name': 'car',
        'keyword': 'Car',
        'categories': ['Private', 'Public transportation'],
        'action_name': 'To be driven',
        'virtual_sensors': [
            {
                'name': 'Magnetic switch sensor',
                'classifier': 'Magnetic Sensor',
                'density_function': 1,
                'measure': 'Car availability',
                'observed_property': 'Car presence on slot',
                'min_value': 0,
                'max_value': 1,
                'sampling_time': 1
            }

        ]
    },
    {
        'name': 'truck',
        'keyword': 'Truck',
        'categories': ['Private', 'Public transportation'],
        'action_name': 'To be driven',
        'virtual_sensors': [
            {
                'name': 'Magnetic switch sensor',
                'classifier': 'Magnetic Sensor',
                'density_function': 1,
                'measure': 'Bike availability',
                'observed_property': 'Bike presence on slot',
                'min_value': 0,
                'max_value': 1,
                'sampling_time': 1
            }

        ]
    }
]

characteristics = ['Color Red', 'Color white', 'Color blue']

# Function to Create Virtual Things

def create_random_virtual_thing(idVirtualThing):
    pre_data = choice(pre_virtual_things)
    ## description = {'A '+ pre_data['name'] + ' is '}
    description = rand_description(words, position, book)
    category = choice(pre_data['categories'])
    identifier = 'Bike ' + str(idVirtualThing)
    alternate_name = 'Bike '
    owned_by = 'Me'
    title = ''
    characteristic = choice(characteristics)

    # Function to Create Virtual Sensors
    virtual_sensor = choice(pre_data['virtual_sensors'])
    # Add data to the sensor
    virtual_thing = {
        'id': idVirtualThing,
        'name': 'VTH' + title.ljust(7 - int(math.log10(idVirtualThing)), '0') + str(idVirtualThing),
        'base': '/api/virtualthings/',
        'name_friendly': alternate_name + str(idVirtualThing),
        'properties':
            {
                'description': "This is a bike", # Add x number of consecutive words here. z = position from which I extract the text (random)
                'category': category,
                'latitude': 37.197055,
                'longitude': -3.6420602,
            }
        ,
        'actions': {
            'admin': "Unknown",
            'description': "Unknown",
        },
        'events':
            {
                'creation': datetime.now(),
            },
        'sensors': [virtual_sensor],
    }
    return virtual_thing


def dynamic_virtual_thing(firebase_db, idVirtualThing):
    virtual_thing_reference = firebase_db.collection('documents').document(str(idVirtualThing))
    retrieved_virtual_thing = virtual_thing_reference.get()
    return retrieved_virtual_thing.to_dict()


def xml_virtual_thing(fire_base_db, retrieved_id):
    virtual_thing = dynamic_virtual_thing(fire_base_db, retrieved_id)
    print(virtual_thing)
    xml_root = ET.Element("virtual_thing")
    comment = ET.Comment('Generated for SIM.WoT Project')
    xml_root.append(comment)
    ET.SubElement(xml_root, "name").text = str(virtual_thing['name'])
    ET.SubElement(xml_root, "base").text = virtual_thing['base']

    properties = ET.SubElement(xml_root, "properties")
    ET.SubElement(properties, "classifier").text = virtual_thing['properties'][0]['category']
    ET.SubElement(properties, "description").text = virtual_thing['properties'][0]['description']

    actions = ET.SubElement(xml_root, "actions")

    events = ET.SubElement(xml_root, "events")
    ET.SubElement(events, "creation").text = virtual_thing['events'][0]['creation']

    sensors = ET.SubElement(xml_root, "sensors")
    ET.SubElement(sensors, "classifier").text = virtual_thing['sensors'][0]['classifier']

    return prettify(xml_root)


########################################################################################################################
