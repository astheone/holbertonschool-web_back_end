#!/usr/bin/env python3
""" 8-all """

def list_all(mongo_collection):
    """
    Lists all documents in a MongoDB collection.

    Args:
        mongo_collection (pymongo.collection.Collection): The collection object.

    Returns:
        list: A list of documents. Returns an empty list if no documents.
    """
    if mongo_collection is None:
        return []
    return list(mongo_collection.find())
