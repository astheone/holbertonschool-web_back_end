#!/usr/bin/env python3
""" 10-update_topics """

def update_topics(mongo_collection, name, topics):
    """
    Changes all topics of a school document based on the name.

    Args:
        mongo_collection (pymongo.collection.Collection): The collection object.
        name (str): The name of the school to update.
        topics (list of str): The list of topics to assign.

    Returns:
        None
    """
    if mongo_collection is None:
        return
    mongo_collection.update_many(
        {"name": name},
        {"$set": {"topics": topics}}
    )
