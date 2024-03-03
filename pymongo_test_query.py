from pandas import DataFrame

# Get the database using the method we defined in pymongo_test_insert file
from pymongo_get_database import get_database
dbname = get_database()
 
# Retrieve a collection named "user_1_items" from database
collection_name = dbname["user_1_items"]
 
item_details = collection_name.find()
for item in item_details:
   # convert the dictionary objects to dataframe
    items_df = DataFrame(item_details)

    # print items
    print(items_df)