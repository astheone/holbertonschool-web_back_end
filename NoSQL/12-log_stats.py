#!/usr/bin/env python3
""" 12-log_stats.py """

from pymongo import MongoClient

if __name__ == "__main__":
    client = MongoClient('mongodb://127.0.0.1:27017')
    db = client.logs
    nginx = db.nginx

    # Total logs
    total_logs = nginx.count_documents({})
    print("{} logs".format(total_logs))

    # Methods count
    print("Methods:")
    methods = ["GET", "POST", "PUT", "PATCH", "DELETE"]
    for method in methods:
        count = nginx.count_documents({"method": method})
        print("\tmethod {}: {}".format(method, count))

    # GET /status
    status_check = nginx.count_documents({"method": "GET", "path": "/status"})
    print("{} status check".format(status_check))
