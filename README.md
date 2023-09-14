<h1 align="center">Python Trojan</h1>
<p align="center"><a href="https://cdn.jsdelivr.net/gh/sindresorhus/awesome@d7305f38d29fed78fa85652e3a63e154dd8e8829/media/badge.svg?label=Repo%20size&style=flat-square"> <img src="https://cdn.jsdelivr.net/gh/sindresorhus/awesome@d7305f38d29fed78fa85652e3a63e154dd8e8829/media/badge.svg?label=Repo%20size&style=flat-square" alt="Awesome" /></a> <a align="center"><a href="https://api.codacy.com/project/badge/Grade/441b48966e9f4b58a643d7c4cee8ba66?label=Repo%20size&style=flat-square"> <img src="https://api.codacy.com/project/badge/Grade/441b48966e9f4b58a643d7c4cee8ba66?label=Repo%20size&style=flat-square" alt="Repo Size" /></a> <a align="center"><a href="https://img.shields.io/github/repo-size/Sasser1337/Trojan.svg?label=Repo%20size&style=flat-square"> <img src="https://img.shields.io/github/repo-size/Sasser1337/Trojan.svg?label=Repo%20size&style=flat-square" alt="Repo Size" /></a></p> </p><p align="center"><a 

<h2 align="center">Simple code of trojan in python :computer:</h2>

<p align="center"><a href="https://github.com/Sasser1337/Trojan/stargazers"><img src="https://img.shields.io/github/stars/Sasser1337/Trojan" alt="Stars Badge"/></a> <a align="center">
<a href="https://github.com/Sasser1337/awesome-github-profile-readme/network/members"><img src="https://img.shields.io/github/forks/Sasser1337/Trojan" alt="Forks Badge"/></a> <a align="center">
<a href="https://github.com/Sasser1337/Trojan/blob/master/LICENSE"><img src="https://img.shields.io/github/license/Sasser1337/Trojan?color=2b9348" alt="License Badge"/></a> <a align="center">

<h2> You need to change the RSS.py code </h2>

```python
server_socket.bind(('0.0.0.0', 8888))
```
<i>How this code works</i>

<h2> Import the necessary modules: </h2>

- [ `socket`: For socket communication.
`subprocess`: For executing commands in the shell. ]

<h2> Initialize the server socket: </h2>

- [ Create a `server_socket` object with socket type `AF_INET` (IPv4) and socket type `SOCK_STREAM` (for TCP connections). ]

- [ Bind the socket to the IP address "0.0.0.0" and port 8888, so the server will listen for connections on that address. ]

<h2> Listen for connections: </h2>

- [ The server starts listening for incoming connections using `server_socket.listen(5)`. This allows up to 5 pending connections. ]

<h2> Accept a client connection: </h2>

- [ When a client connection is accepted, the server executes `server_socket.accept()`, which will block the program until there's an incoming connection. When a connection is made, it returns a `client_socket` object used for communication with the client and the client's `addr`. ]

<h2> Main loop: </h2>
- [ The server enters an infinite loop to receive commands from the client. ]

<h2> Receive a command from the client: </h2>

- [ The server receives a command from the client using `client_socket.recv(1024)`. The received data is decoded into a string. ]

<h2> Execute the command: </h2>

- [ If the received command is "exit," the server will close the connection with the client and exit the loop.
If the command is any other shell command, the server will execute that command in the shell using `subprocess.check_output()`. The output of the command is sent back to the client through `client_socket`. ]

<h2> Handle errors: </h2>

- [ If there is an error while executing a command, the server captures the error and sends an error message back to the client. ]

<h2> Close the connection: </h2>

- [ After the client sends the "exit" command or if there's an unhandled error, the server will close the connection with the client using `client_socket.close()`. ]

<h2> Close the server socket: </h2>

- [ After finishing, the server socket is closed using `server_socket.close()`. ]

- [ I haven't tried this program, maybe you should try it yourself ]
