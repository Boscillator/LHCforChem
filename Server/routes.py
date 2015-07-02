"""
Contains routes
"""

from Server import app
from flask import render_template

@app.route('/')
def home():
    return render_template('home.html', sections = app.config["models"])

@app.route('/section/<int:id>')
def section(id):
    s = app.config["models"][id]
    return render_template('section.html', section = s, id=id)
