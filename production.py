"""
Runnes server for production use
"""

from Server import app

app.run(host='0.0.0.0',port=80)