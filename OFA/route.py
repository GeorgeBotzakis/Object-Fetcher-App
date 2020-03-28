from OFA import app
from flask import render_template, request, Response, redirect, url_for, session
import os

@app.route('/home', methods=['GET', 'POST'])
def home(name="Georgie"):
    return render_template("index.html", content=name)