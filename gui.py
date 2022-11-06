import find, insert, delete
from flask import Flask, render_template, request, url_for, flash, redirect

app = Flask(__name__)

@app.route('/', methods=('GET','POST'))
def index():
    if request.method == 'POST':
        print('post method')
        if not request.form.get('NewTask') == None:
            print('insert one')
            insert.one(request.form['NewTask'])
        
        if not request.form.get('ID') == None:
            print('delete one')
            print(request.form["ID"])
            delete.one(request.form["ID"])
        
        return redirect(url_for('index'))
    return render_template('list.html',reminders=find.all())