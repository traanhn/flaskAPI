import sqlite3
import json
import os


def initial_load():
    insert_user_query = "INSERT INTO users VALUES (?, ?, ?, ?, ?, ?, ?)"
    truncate_user_query = "DELETE FROM users"
    with open(os.path.join('data','data.json')) as fp:
        data = json.load(fp)
        with sqlite3.connect("data.db") as conn:
            conn.execute(truncate_user_query)
            keys = data[0].keys()
            for entry in data:
                values = [entry.get(key, None) for key in keys]
                conn.execute(insert_user_query, values)
                conn.commit()
