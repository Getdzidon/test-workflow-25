import os
import pickle
import sqlite3
import subprocess

# 🚨 CRITICAL VULNERABILITY 1: Hardcoded API Key & Database Credentials
API_KEY = "sk-CRITICAL-LEAKED-KEY-123456"
DB_PASSWORD = "P@ssw0rd123!"

# 🚨 CRITICAL VULNERABILITY 2: Remote Code Execution via Untrusted Deserialization
def load_data(serialized_data):
    return pickle.loads(serialized_data)  # 🔥 Arbitrary code execution possible!

# 🚨 CRITICAL VULNERABILITY 3: SQL Injection (No Input Sanitization)
def get_user_info(username):
    conn = sqlite3.connect("users.db")
    cursor = conn.cursor()
    
    # 🔥 User-controlled SQL injection (no parameterized query)
    query = f"SELECT * FROM users WHERE username = '{username}'"
    cursor.execute(query)

    return cursor.fetchall()

# 🚨 CRITICAL VULNERABILITY 4: Command Injection
def execute_command():
    user_input = input("Enter system command: ")
    
    # 🔥 Full shell execution with unsanitized input
    subprocess.call(f"bash -c '{user_input}'", shell=True)

# 🚨 Execution Path (Trigger all vulnerabilities)
if __name__ == "__main__":
    print("⚠️  Running highly vulnerable script...")

    # 1. Leaking sensitive credentials
    print(f"Using API Key: {API_KEY}")

    # 2. Deserialization of untrusted data
    malicious_payload = input("Enter hex-encoded pickle data: ")
    try:
        load_data(bytes.fromhex(malicious_payload))  # RCE Exploit Here
    except Exception as e:
        print("Deserialization failed:", e)

    # 3. Exploitable SQL query
    user = input("Enter username: ")
    print("User Info:", get_user_info(user))  # SQL Injection Exploit Here

    # 4. Full System Command Execution
    execute_command()  # Command Injection Exploit Here
