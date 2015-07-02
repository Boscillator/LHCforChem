from Server.loadXml import loadXML


f = open("config.xml")
sections = loadXML(f.read())

print sections


for section in sections:
    print "======================="
    print "Name: "+section.name
    print "Disc: "+section.disc
    print "Tags-------------------"
    for tag in section.tags:
        print "\t"+tag
    print "Resources--------------"
    for resource in section.resources:
        print "\t-------------------"
        print "\tHREF: "+resource.href
        print "\tType: "+resource.resourceType
        print "\tName: "+resource.name
        print "\tDisc: "+resource.disc