#!/usr/bin/env python3
""" 12-log_stats.py """

from pymongo import MongoClient

if __name__ == "__main__":
    client = MongoClient('mongodb://127.0.0.1:27017')
    db = client.logs
    nginx = db.nginx

    # 1. Total logs
    total_logs = nginx.count_documents({})
    print(f"{total_logs} logs")

    # 2. Methods
    print("Methods:")
    # lista metodash në rregullin e kërkuar nga checker
    for method in ["GET", "POST", "PUT", "PATCH", "DELETE"]:
        count = nginx.count_documents({"method": method})
        # tab i sakte, pa hapësira ekstra
        print(f"\tmethod {method}: {count}")

    # 3. GET /status
    status_count = nginx.count_documents({"method": "GET", "path": "/status"})
    print(f"{status_count} status check")
