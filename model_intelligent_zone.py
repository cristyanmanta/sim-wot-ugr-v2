import xml.etree.ElementTree as ET
from xml.etree import ElementTree
from xml.dom import minidom


def prettify(elem):
    """Return a pretty-printed XML string for the Element.
    """
    rough_string = ElementTree.tostring(elem, 'utf-8')
    reparsed = minidom.parseString(rough_string)
    return reparsed.toprettyxml(indent="  ")


static_description = "officially the Kingdom of Spain (Spanish: Reino de España),[d][e] is a sovereign state and " \
                     "a member state of the European Union. It is located on the Iberian Peninsula in southwestern " \
                     "Europe. Its mainland is bordered to the south and east by the Mediterranean Sea except for a " \
                     "small land boundary with Gibraltar; to the north and north east by France, Andorra, and the " \
                     "Bay of Biscay; and to the west and northwest by Portugal and the Atlantic Ocean. It is one of " \
                     "three countries—France and Morocco are the other two—to have both Atlantic and Mediterranean " \
                     "coastlines. Spain's 1,214 km (754 mi) border with Portugal is the longest uninterrupted border " \
                     "within the European Union.)"


intelligent_zone = {
    'name': 'izn0001',
    'base': '/api/intellizones/',
    'properties': [
        {
            'keyword': 'Europe, Spain, Country, Kingdom',
            'classifier': 'Country',
            'description': static_description,
            'location_name': 'Reino de España',
            'address': 'C/ Panama, 1, 28046 Madrid',
            'geo_class': '(A) Country, State, Region, ...',
            'geo_identifier': '2510769',
            'feature_code': '(PCLI) Independent Political Entity',
            'latitude': 40.0000,
            'longitude': -4.0000,
            'elevation': 532,
            'membership': 'Root',
        }
    ],
    'actions': [
        {
            'admin': 'Ministerio de industria, energía y turismo',
             'description': 'Contain Smart Spaces'
            }
        ]
    }


def json_intelligent_zone():
    return intelligent_zone


def xml_intelligent_zone():

    xml_root = ET.Element("intelligent_zone")
    comment = ET.Comment('Generated for SIM.WoT Project')
    xml_root.append(comment)
    ET.SubElement(xml_root, "name").text = intelligent_zone['name']
    ET.SubElement(xml_root, "base").text = intelligent_zone['base']

    properties = ET.SubElement(xml_root, "properties")
    ET.SubElement(properties, "keyword").text = intelligent_zone['properties'][0]['keyword']
    ET.SubElement(properties, "classifier").text = intelligent_zone['properties'][0]['classifier']
    ET.SubElement(properties, "description").text = intelligent_zone['properties'][0]['description']
    ET.SubElement(properties, "location_name").text = intelligent_zone['properties'][0]['location_name']
    ET.SubElement(properties, "address").text = intelligent_zone['properties'][0]['address']
    ET.SubElement(properties, "geo_class").text = intelligent_zone['properties'][0]['geo_class']
    ET.SubElement(properties, "geo_identifier").text = intelligent_zone['properties'][0]['geo_identifier']
    ET.SubElement(properties, "feature_code").text = intelligent_zone['properties'][0]['feature_code']
    ET.SubElement(properties, "latitude").text = str(intelligent_zone['properties'][0]['latitude'])
    ET.SubElement(properties, "longitude").text = str(intelligent_zone['properties'][0]['longitude'])
    ET.SubElement(properties, "elevation").text = str(intelligent_zone['properties'][0]['elevation'])
    ET.SubElement(properties, "membership").text = intelligent_zone['properties'][0]['membership']

    actions = ET.SubElement(xml_root, "actions")
    ET.SubElement(actions, "admin").text = intelligent_zone['actions'][0]['admin']
    ET.SubElement(actions, "description").text = intelligent_zone['actions'][0]['description']

    return prettify(xml_root)

########################################################################################################################


