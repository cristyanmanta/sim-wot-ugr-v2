import xml.etree.ElementTree as ET
from xml.etree import ElementTree
from xml.dom import minidom


def prettify(elem):
    """Return a pretty-printed XML string for the Element.
    """
    rough_string = ElementTree.tostring(elem, 'utf-8')
    reparsed = minidom.parseString(rough_string)
    return reparsed.toprettyxml(indent="  ")


static_description = "Barcelona is the capital city of the autonomous community of Catalonia in Spain and the " \
                     "country's 2nd largest city, with a population of 1.6 million[1] within its administrative " \
                     "limits. Its urban area extends beyond the administrative city limits with a population of " \
                     "around 4.5 million people, being the sixth-most populous urban area in the European Union " \
                     "after Paris, London, Madrid, the Ruhr area and Milan. About five million[2][3][4][5][6] people " \
                     "live in the Barcelona metropolitan area. It is the largest metropolis on the Mediterranean " \
                     "Sea, located on the coast between the mouths of the rivers Llobregat and Besòs, and bounded " \
                     "to the west by the Serra de Collserola mountain range, the tallest peak of which is 512 metres " \
                     "(1,680 ft) high."


smart_space = {
    'name': 'ssp0001',
    'base': '/api/smartspaces/',
    'properties': [
        {
            'keyword': 'Spain, Catalonia, City',
            'classifier': 'City',
            'description': static_description,
            'location_name': 'Barcelona',
            'address': 'Pl. Sant Jaume, 1, 08002',
            'geo_class': '(P) City, Village',
            'geo_identifier': '3128760',
            'feature_code': '(PPLA) Seat of a First-Order Administrative Division',
            'latitude': 41.2320,
            'longitude': 2.0932,
            'elevation': 15,
            'membership': 'api/intellizones?id=izn0001',
        }
    ],
    'actions': [
        {
            'admin': 'Ajuntament de Barcelona',
            'description': 'Contain Smart Sub Spaces'
            }
        ]
    }


def json_smart_space():
    return smart_space


def xml_smart_space():

    xml_root = ET.Element("smart_space")
    comment = ET.Comment('Generated for SIM.WoT Project')
    xml_root.append(comment)
    ET.SubElement(xml_root, "name").text = smart_space['name']
    ET.SubElement(xml_root, "base").text = smart_space['base']

    properties = ET.SubElement(xml_root, "properties")
    ET.SubElement(properties, "keyword").text = smart_space['properties'][0]['keyword']
    ET.SubElement(properties, "classifier").text = smart_space['properties'][0]['classifier']
    ET.SubElement(properties, "description").text = smart_space['properties'][0]['description']
    ET.SubElement(properties, "location_name").text = smart_space['properties'][0]['location_name']
    ET.SubElement(properties, "address").text = smart_space['properties'][0]['address']
    ET.SubElement(properties, "geo_class").text = smart_space['properties'][0]['geo_class']
    ET.SubElement(properties, "geo_identifier").text = smart_space['properties'][0]['geo_identifier']
    ET.SubElement(properties, "feature_code").text = smart_space['properties'][0]['feature_code']
    ET.SubElement(properties, "latitude").text = str(smart_space['properties'][0]['latitude'])
    ET.SubElement(properties, "longitude").text = str(smart_space['properties'][0]['longitude'])
    ET.SubElement(properties, "elevation").text = str(smart_space['properties'][0]['elevation'])
    ET.SubElement(properties, "membership").text = smart_space['properties'][0]['membership']

    actions = ET.SubElement(xml_root, "actions")
    ET.SubElement(actions, "admin").text = smart_space['actions'][0]['admin']
    ET.SubElement(actions, "description").text = smart_space['actions'][0]['description']

    return prettify(xml_root)


########################################################################################################################


