from flask import Flask, render_template, request, url_for, flash, redirect
from pymongo.mongo_client import MongoClient
from pymongo.server_api import ServerApi
import cfg

# Create a new client and connect to the server
client = MongoClient(cfg.db_uri, server_api=ServerApi('1'))

# Send a ping to confirm a successful connection
try:
    client.admin.command('ping')
    print("Pinged your deployment. You successfully connected to MongoDB!")
except Exception as e:
    print(e)

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