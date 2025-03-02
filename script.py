import os

# 🚨 CRITICAL VULNERABILITY: Hardcoded API Key
API_KEY = "sk-1234567890abcdefg"  # Sensitive key exposed
DB_PASSWORD = "SuperSecretPassword123"  # Hardcoded database password

# 🚨 CRITICAL VULNERABILITY: Remote Code Execution (RCE)
user_input = input("Enter a command: ")

# Evaluates user input as Python code (EXTREMELY DANGEROUS)
result = eval(user_input)

print("Result:", result)

# 🚨 API key is used in an insecure way
url = f"https://example.com/api?key={API_KEY}"
response = os.system(f"curl -s {url}")  # Insecure API request
print("API Response:", response)
