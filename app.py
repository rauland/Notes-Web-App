from flask import Flask, render_template
import pandas as pd

from pymongo_get_database import get_database
dbname = get_database()

# Retrieve a collection named "user_1_items" from database
collection_name = dbname["user_1_items"]

app = Flask(__name__)

@app.route("/")
def index():
    item_details = collection_name.find()
    item_list = []
    for item in item_details:
        item_list.append(item['item_name'])
        print (item['item_name'])
        # convert the dictionary objects to dataframe
        # items_df = pd.DataFrame(item_details)
        # print(items_df)
    return render_template('app.html',notes=item_list)

@app.route('/about')
def about():
    return render_template('about.html')