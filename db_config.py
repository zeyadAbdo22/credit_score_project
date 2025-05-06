# MySQL connection setup
# db_config.py
import mysql.connector

def get_all_connections():
    config = {
        "host": "localhost",
        "user": "root",
        "password": ""
    }

    databases = ["users_db", "payments_db", "debt_db", "history_db", "mix_db"]
    conns = {}
    for db in databases:
        conn = mysql.connector.connect(database=db, **config)
        conns[db] = conn
    return conns