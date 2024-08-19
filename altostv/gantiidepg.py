import xml.etree.ElementTree as ET

# Read the XML file content as a string
print('Resymboling channel IDs and format the output')
with open('apa.xml', 'r') as file:
    xml_string = file.read()

# Parse the XML string
root = ET.fromstring(xml_string)

# Iterate through each 'channel' element and print the 'id' and 'display-name'
for channel in root.findall('channel'):
    channel_id = channel.get('id')  # Get the 'id' attribute
    display_name = channel.find('display-name').text  # Get the text of 'display-name'
    xml_string = xml_string.replace(f'"{channel_id}"', f'"{display_name.replace(' ', '')}.Id"')


f = open("tv.xml", "w")
f.write(xml_string)
f.close()
