import requests
from xml.etree import ElementTree as ET

url = "http://localhost:8085/data.xml"  # si activas el servidor en OHM
response = requests.get(url)
xml_root = ET.fromstring(response.content)

for sensor in xml_root.findall(".//Sensor"):
    if sensor.attrib.get("Type") == "Temperature":
        print(f"{sensor.attrib['Name']}: {sensor.attrib['Value']} °C")
