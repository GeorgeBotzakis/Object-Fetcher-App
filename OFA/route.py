from OFA import app
from flask import render_template, request, Response, redirect, url_for, session, flash, send_from_directory
from werkzeug.utils import secure_filename
import os
import time
from OFA.predictionScript import run_prediction

ALLOWED_EXTENSIONS = set(['png', 'jpg', 'jpeg'])

# don't keep cache, any time it's play the current video
# @app.after_request
# def add_header(r):
#     """
#     Add headers to both force latest IE rendering engine or Chrome Frame,
#     and also to cache the rendered page for 10 minutes.
#     """
#     r.headers["Cache-Control"] = "no-cache, no-store, must-revalidate"
#     r.headers["Pragma"] = "no-cache"
#     r.headers["Expires"] = "0"
#     r.headers['Cache-Control'] = 'public, max-age=0'
#     return r

# @app.route('/uploads/<path:filename>%t=<curr_time>')
# def get_output_image(filename, curr_time):
#     return send_from_directory("../" + app.config['OUTPUT_FOLDER'], filename)

def allowed_file(filename):
    return '.' in filename and filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS
def convertTuple(tup): 
    str =  ''.join(tup)
    return str

@app.route('/home', methods=['GET', 'POST'])
def home(name="Georgie"):
    print("aaa")
    #main11()
    if request.method == 'POST':
        if 'file' not in request.files:
            flash('No file part')
            return redirect(request.url)
        file = request.files['file']
        if file.filename == '':
            flash('No selected file')
            return redirect(request.url)
        if file and allowed_file(file.filename):
            filename = secure_filename(file.filename)
            file.save(os.path.join(app.config['UPLOAD_FOLDER'], filename))
            print(app.config['UPLOAD_FOLDER'], filename)
            v_labels, output_filename = run_prediction(os.path.join(app.config['UPLOAD_FOLDER'], filename))

            if len(v_labels) > 1:
                comma_sep = ','.join(v_labels)
            elif len(v_labels) == 1:
                comma_sep = v_labels[0]
            else:
                comma_sep="none"

            curr_time = int(time.time())
            print(output_filename)
            print(comma_sep)

            return redirect(url_for('results',name="JEORG", labels=comma_sep, epoch_time=curr_time, filename=output_filename))
            
    return render_template("index.html", content=name)

# @app.route('/uploads/<filename>')
# def uploaded_file(filename):
#     print(filename)
#     print(app.config['UPLOAD_FOLDER'])
#     print(app.config['OUTPUT_FOLDER'])
#     print(app.config['OUTPUT_FOLDER'])
#     return send_from_directory("../" + app.config['OUTPUT_FOLDER'], 'output.png')



@app.route('/results', methods=['GET', 'POST'])
def results(name="non", labels=list(), epoch_time=0000, filename="no filename"):
    # filename = secure_filename('output.png')
    # imgPath=os.path.join(app.config['OUTPUT_FOLDER'], filename)
    filename = request.args['filename']
    labels = request.args['labels']
    print(labels)
    print(filename)
    name = "JEORG"
    #filename="http://0.0.0.0:5000/uploads/output.png"
    curr_img = os.path.join(app.config['OUTPUT_FOLDER'], filename)
    print(curr_img)
    # myPath = "static/images/output2.png"

    return render_template("results.html", content=name, output_img=curr_img)