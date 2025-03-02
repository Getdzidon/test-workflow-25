import pickle

# 🚨 Critical Vulnerability: Unsafe deserialization (Remote Code Execution)
data = input("Enter serialized data: ")

# Directly loading untrusted data (extremely dangerous!)
obj = pickle.loads(bytes.fromhex(data))

print("Deserialized object:", obj)
