from pymongo import MongoClient

client = MongoClient()
test_object = {'a': '1', 'b':'2','c':'3'}
my_collection = client.my_database.my_collection

def find_object(primary_key):
    """Finds and returns an object matching the primary key.
    Returns None if not found.
    """
    my_object = my_collection.find_one({'a':primary_key})
    return my_object

def update_object(new_object):
    """Update an object if exists, inster if it does not exists.
    """
    my_collection.update({'a':new_object['a']}, test_object, upsert=True)

def remove_object(primary_key):
    """Delete the object matching primary key.
    Returns True if deleted, False if not found.
    """
    del_result = my_collection.delete_one({'a':primary_key})
    return del_result.deleted_count > 0
