import urllib.request
import certifi
import xml.etree.ElementTree as ET

#url="http://python-data.dr-chunk.net/comments_200531.xml"
#xml=urllib.request.urlopen(url).read()

with urllib.request.urlopen("https://www.google.com/sitemap.xml", cafile=certifi.where()) as url:
    xml = url.read()
    print("Retrieved "+ str(len(xml)) + " characters")
    e=ET.XML(xml)
    output=e.findall('loc')
    print(output)
    print(e)