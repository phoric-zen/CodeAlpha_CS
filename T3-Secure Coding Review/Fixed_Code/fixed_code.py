# secure_app.py

import subprocess
import shlex
import sqlite3

def safe_command_execution(command):
    try:
        result = subprocess.run(shlex.split(command), capture_output=True, text=True, check=True)
        return result.stdout
    except Exception as e:
        return str(e)

def safe_sql_query(username):
    conn = sqlite3.connect("users.db")
    cursor = conn.cursor()
    query = "SELECT * FROM users WHERE username = ?"
    cursor.execute(query, (username,))
    return cursor.fetchall()

# Dangerous functions like eval and pickle.loads removed
