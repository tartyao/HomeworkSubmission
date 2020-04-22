from flask import Flask, render_template, request
import os
from werkzeug.utils import secure_filename

app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def index():
  if request.method == "GET":
    return render_template("index.html")
  else:
    message = 'Homework Submitted'
    name = request.form.get('name')
    classs = request.form.get('classs')
    photo = request.files['photo']
    filename = secure_filename(photo.filename)
    path = os.path.join('uploads', filename)
    photo.save(path)
    date = request.form.get('date')
    fout = open("Submission.txt", 'a')
    fout.write(name + ' | ' + classs + ' | ' + filename + ' | ' + date + '\n' )
    fout.close()
    return render_template('index.html', message = message, name=name,classs=classs, date=date, filename=filename)

    
app.run(host='0.0.0.0', port=8080)
