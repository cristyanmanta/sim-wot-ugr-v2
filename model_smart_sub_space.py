import xml.etree.ElementTree as ET
from xml.etree import ElementTree
from xml.dom import minidom
from sim_wot_db_connection import sim_wot_marshall


def prettify(elem):
    """Return a pretty-printed XML string for the Element.
    """
    rough_string = ElementTree.tostring(elem, 'utf-8')
    reparsed = minidom.parseString(rough_string)
    return reparsed.toprettyxml(indent="  ")


def dynamic_smart_sub_space(db, retrieved_entity, retrieved_id):
    entity_type = "smart_sub_space"
    entity = sim_wot_marshall(db, entity_type, retrieved_entity, retrieved_id)
    static_description = entity["description"]
    smart_sub_space = {
        'name': entity["id"],
        'base': '/api/smartsubspaces/',
        'properties': [
            {
                'keyword': entity["keyword"],
                'classifier': entity["classifier"],
                'description': static_description,
                'location_name': entity["location_name"],
                'address': entity["address"],
                'geo_class': entity["geo_class"],
                'geo_identifier': entity["geo_identifier"],
                'feature_code': entity["feature_code"],
                'latitude': entity["latitude"],
                'longitude': entity["longitude"],
                'elevation': entity["elevation"],
                'membership': entity["membership"],
            }
        ],
        'actions': [
            {
                'admin': 'Ajuntament de Barcelona',
                'description': 'Contain virtual Things'
                }
            ]
        }
    return smart_sub_space


def json_smart_sub_space(db, retrieved_entity, retrieved_id):
    smart_sub_space = dynamic_smart_sub_space(db, retrieved_entity, retrieved_id)
    return smart_sub_space


def xml_smart_sub_space(db, retrieved_entity,retrieved_id):
    smart_sub_space = dynamic_smart_sub_space(db, retrieved_entity, retrieved_id)
    xml_root = ET.Element("smart_sub_space")
    comment = ET.Comment('Generated for SIM.WoT Project')
    xml_root.append(comment)
    ET.SubElement(xml_root, "name").text = smart_sub_space['name']
    ET.SubElement(xml_root, "base").text = smart_sub_space['base']

    properties = ET.SubElement(xml_root, "properties")
    ET.SubElement(properties, "keyword").text = smart_sub_space['properties'][0]['keyword']
    ET.SubElement(properties, "classifier").text = smart_sub_space['properties'][0]['classifier']
    ET.SubElement(properties, "description").text = smart_sub_space['properties'][0]['description']
    ET.SubElement(properties, "location_name").text = smart_sub_space['properties'][0]['location_name']
    ET.SubElement(properties, "address").text = smart_sub_space['properties'][0]['address']
    ET.SubElement(properties, "geo_class").text = smart_sub_space['properties'][0]['geo_class']
    ET.SubElement(properties, "geo_identifier").text = smart_sub_space['properties'][0]['geo_identifier']
    ET.SubElement(properties, "feature_code").text = smart_sub_space['properties'][0]['feature_code']
    ET.SubElement(properties, "latitude").text = str(smart_sub_space['properties'][0]['latitude'])
    ET.SubElement(properties, "longitude").text = str(smart_sub_space['properties'][0]['longitude'])
    ET.SubElement(properties, "elevation").text = str(smart_sub_space['properties'][0]['elevation'])
    ET.SubElement(properties, "membership").text = smart_sub_space['properties'][0]['membership']

    actions = ET.SubElement(xml_root, "actions")
    ET.SubElement(actions, "admin").text = smart_sub_space['actions'][0]['admin']
    ET.SubElement(actions, "description").text = smart_sub_space['actions'][0]['description']

    return prettify(xml_root)


########################################################################################################################


