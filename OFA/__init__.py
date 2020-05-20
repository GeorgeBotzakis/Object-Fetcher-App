from flask import Flask

import os

UPLOAD_FOLDER = 'OFA/input-images'
OUTPUT_FOLDER = 'static/output-images'

app = Flask(__name__)
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER
app.config['OUTPUT_FOLDER'] = OUTPUT_FOLDER

app.secret_key = os.urandom(24)



from OFA import route
from OFA.predictObjects import run_prediction

# database models go here
