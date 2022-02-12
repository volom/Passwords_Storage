import sqlite3
import os
import pandas as pd
from datetime import datetime

conn = sqlite3.connect(f'{os.getcwd()}//db_repo//password_db.db', check_same_thread = False)
cur = conn.cursor()

def try_connect():
    try:
        cur.execute("SELECT * FROM passwords")
        conn.commit()
        return "connected"
    except Exception as e:
        return str(e)

def get_all_passwords() -> list:
    cur.execute("SELECT * FROM passwords")
    return cur.fetchall()

def add_password(profile, login, password):
    try:
        cur.execute(f"""INSERT INTO passwords (profile, login, password, date_added) VALUES ("{profile}", "{login}", "{password}", "{datetime.now().strftime("%Y-%m-%d %H:%M:%S")}")""")
        conn.commit()
    except:
        cur.execute(f"""
                     UPDATE passwords 
                     SET login = "{login}", password = "{password}", date_added = "{datetime.now().strftime("%Y-%m-%d %H:%M:%S")}"
                     WHERE profile = "{profile}"
                     """)
        conn.commit()      