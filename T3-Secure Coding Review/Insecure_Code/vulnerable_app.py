# vulnerable_app.py

import os
import pickle
import sqlite3

# Hardcoded secret
API_KEY = "1234567890abcdef"

def dangerous_eval(user_input):
    return eval(user_input)  # Insecure use of eval()

def dangerous_pickle(data):
    return pickle.loads(data)  # Vulnerable to arbitrary code execution

def run_system_command(command):
    os.system(command)  # Command injection

def insecure_sql_query(username):
    conn = sqlite3.connect("users.db")
    cursor = conn.cursor()
    query = f"SELECT * FROM users WHERE username = '{username}'"  # SQL Injection
    cursor.execute(query)
    return cursor.fetchall()
