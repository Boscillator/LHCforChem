"""
Main file for LHCforChem
Does inizilization
"""

from flask import Flask
from loadXml import loadXML

app = Flask(__name__)

f = open("../config.xml")
app.config["models"] = loadXML(f.read())
f.close()