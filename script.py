import os

# Get user input for a file to list
filename = input("Enter the filename to list: ")

# 🚨 Critical vulnerability: Command Injection!
os.system(f"ls -l {filename}")
