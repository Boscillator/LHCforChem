import xml.etree.cElementTree as et

class XmlBase(object):
    pass

class Resource(XmlBase):
    
    def __init__(self, href, resourecType, name, disc):
        self.href = href
        self.resourceType = resourecType
        self.name = name
        self.disc = disc
    
class Section(XmlBase):
    
    def __init__(self, name, disc):
        self.name = name
        self.disc = disc
        self.tags = []
        self.resources = []
    

def loadXML(xml):
    tree = et.fromstring(xml)
    sections = []
    for el in tree.findall('section'):
        sections.append(None)
        #print "-"
        name = el.attrib["name"]
        disc = el.attrib["disc"]
        sections[-1] = Section(name,disc)
        for ch in el.getchildren():
            #print ch.tag
            if ch.tag == "tag":
                sections[-1].tags.append(ch.text)
            elif ch.tag == "resource":
                href = ch.attrib["href"]
                resourceType = ch.attrib["type"]
                name = ch.attrib["name"]
                disc = ch.attrib["disc"]
                sections[-1].resources.append(Resource(href,resourceType,name,disc))
        
    return sections
    
    
    
    
    