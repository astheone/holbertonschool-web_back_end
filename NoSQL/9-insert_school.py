#!/usr/bin/env python3
""" 9-insert_school """

def insert_school(mongo_collection, **kwargs):
    """
    Inserts a new document in a MongoDB collection based on kwargs.

    Args:
        mongo_collection (pymongo.collection.Collection): The collection object.
        **kwargs: key/value pairs of the document to insert.

    Returns:
        The _id of the inserted document.
    """
    if mongo_collection is None:
        return None
    result = mongo_collection.insert_one(kwargs)
    return result.inserted_id
