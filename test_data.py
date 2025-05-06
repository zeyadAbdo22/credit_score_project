# test_data.py
import mysql.connector
import random

config = {
    "host": "localhost",
    "user": "root",
    "password": "",
}

def insert_data():
    for user_id in range(1, 11):  
        name = f"Client{user_id}"
        on_time = random.randint(5, 12)
        total = random.randint(on_time, 15)
        used = random.randint(1000, 8000)
        credit_limit = random.randint(used + 1000, 15000)
        account_age = random.randint(6, 60)  
        types_used = random.randint(1, 4)
        total_types = random.randint(types_used, 5)

        data = {
            "users_db": f"INSERT INTO users (user_id, name) VALUES ({user_id}, '{name}')",
            "payments_db": f"INSERT INTO payments (user_id, on_time, total) VALUES ({user_id}, {on_time}, {total})",
            "debt_db": f"INSERT INTO debt (user_id, used, credit_limit) VALUES ({user_id}, {used}, {credit_limit})",
            "history_db": f"INSERT INTO history (user_id, account_age) VALUES ({user_id}, {account_age})",
            "mix_db": f"INSERT INTO credit_mix (user_id, types_used, total_types) VALUES ({user_id}, {types_used}, {total_types})"
        }

        for db, sql in data.items():
            conn = mysql.connector.connect(database=db, **config)
            cursor = conn.cursor()
            cursor.execute(sql)
            conn.commit()
            conn.close()

insert_data()
