from Server.loadXml import loadXML


f = open("config.xml")
sections = loadXML(f.read())

print sections


for section in sections:
    for resource in section.resources:
        print resource.search