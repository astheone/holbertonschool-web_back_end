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
    print("\tmethod GET: {}".format(nginx.count_documents({"method": "GET"})))
    print("\tmethod POST: {}".format(nginx.count_documents({"method": "POST"})))
    print("\tmethod PUT: {}".format(nginx.count_documents({"method": "PUT"})))
    print("\tmethod PATCH: {}".format(nginx.count_documents({"method": "PATCH"})))
    print("\tmethod DELETE: {}".format(nginx.count_documents({"method": "DELETE"})))

    # GET /status count
    status_check = nginx.count_documents({"method": "GET", "path": "/status"})
    print("{} status check".format(status_check))
