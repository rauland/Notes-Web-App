from pymongo.mongo_client import MongoClient
from pymongo.server_api import ServerApi
import cfg

def get_database():
    # Create a new client and connect to the server
    client = MongoClient(cfg.db_uri, server_api=ServerApi('1'))

    # Send a ping to confirm a successful connection
    try:
        client.admin.command('ping')
        print("Pinged your deployment. You successfully connected to MongoDB!")
    except Exception as e:
        print(e)

    # Get the database for the "user_note_list" collection.
    return client['user_note_list']

if __name__ == "__main__":
    dbname = get_database()