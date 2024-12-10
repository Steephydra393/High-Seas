# Run this file to start the game's website

'''
The way I normaly set up a flask:
project
    - /client
        - frontend.py
            - frontend_blueprint
            
    - /server
        - backend.py
            - backend_blueprint
            
    - main.py
        - main app file


You will see this is consistent in all my projects, its mainly to have consistency in my projects, and to make it easier to manage the project.

Authors:
Joseph L. aka Steephydra

Project start date:
12/9/2024

Project end date:
TBD/TBD/TBD
'''

from flask import Flask, render_template, blueprints
from datetime import datetime
from server.backend import backend_blueprint
from client.frontend import frontend_blueprint

app = Flask(__name__)

app.register_blueprint(backend_blueprint, url_prefix="/api")
app.register_blueprint(frontend_blueprint)

if __name__ == '__main__':
    app.run(debug=True)
    