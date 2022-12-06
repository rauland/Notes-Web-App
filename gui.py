import find, insert, delete
from flask import Flask, render_template, request, url_for, flash, redirect

app = Flask(__name__)

@app.route('/', methods=('GET','POST'))
def index():
    if request.method == 'POST':
        print('post method')
        if not request.form.get('NewTask') == None:
            print('insert one')
            if not request.form['NewTask'] == "":
                insert.one(request.form['NewTask'])
        
        if not request.form.get('ID') == None:
            print('delete one')
            print(request.form["ID"])
            delete.one(request.form["ID"])
        
        return redirect(url_for('index'))
    return render_template('app.html',reminders=find.all())