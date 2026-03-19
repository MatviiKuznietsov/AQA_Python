import xml.etree.ElementTree as ET
import logging

logging.basicConfig(level=logging.INFO)

def find_incoming_by_group(xml_file, group_number):

    tree = ET.parse(xml_file)
    root = tree.getroot()

    for group in root.findall("group"):

        number = group.find("number")

        if number is not None and number.text == str(group_number):

            incoming = group.find("timingExbytes/incoming")

            if incoming is not None:
                logging.info(f"incoming for group {group_number}: {incoming.text}")
                return incoming.text

    logging.info("Group not found")


xml_file = "groups.xml"

find_incoming_by_group(xml_file, 2)