import xml.etree.cElementTree as et

class XmlBase(object):
    """
    Xml base object
    (Not used)
    """
    pass

class Resource(XmlBase):
    """
    Rousource Model
    """
    def __init__(self, href, resourecType, name, disc, section, searchURL=None):
        self.href = href
        self.resourceType = resourecType
        self.name = name
        self.disc = disc
        self.section = section
        self.search = open(searchURL).read()
          
class Section(XmlBase):
    """
    Section Model
    """
    def __init__(self, name, disc):
        self.name = name
        self.disc = disc
        self.tags = []
        self.resources = []
    

def loadXML(xml):
    """
    Loads models from xml pased in by string
    """
    tree = et.fromstring(xml)   #Get Tree
    sections = []
    for el in tree.findall('section'):  #Loop through all sections
        sections.append(None)   #Makes the list one longer
        #print "-"
        name = el.attrib["name"]    #Set up section
        disc = el.attrib["disc"]
        sections[-1] = Section(name,disc)   #Create Section at position created when list was made longer
        for ch in el.getchildren(): #Loop through tags and resources
            #print ch.tag
            if ch.tag == "tag": #If it's a tag add it's text to the tag list of the current section (The one created by sections.append(None))
                sections[-1].tags.append(ch.text)
            elif ch.tag == "resource":  #If it's a resouce get attribs, and append a new Resouce to the current sections resources list
                href = ch.attrib["href"]
                resourceType = ch.attrib["type"]
                name = ch.attrib["name"]
                disc = ch.attrib["disc"]
                search = ch.attrib["search"]
                sections[-1].resources.append(Resource(href,resourceType,name,disc,sections[-1],search))
        
    return sections
    
    
    
    
    