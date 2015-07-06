"""
Contains routes
"""

from Server import app
from flask import render_template, request


@app.route('/')
def home():
    return render_template('home.html', sections = app.config["models"])

@app.route('/section/<int:id>')
def section(id):
    s = app.config["models"][id]
    return render_template('section.html', section = s, id=id)

@app.route('/search',methods=['POST'])
def search():
    query = request.form["search"].lower()
    resources=[]
    for section in app.config["models"]:
        for resource in section.resources:
            if query in resource.search or query in resource.name or query in resource.disc:
                resources.append(resource)
                
    return render_template("search.html",resources=resources)

