
import socket
import os

# create a socket object 
server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
print("socket successfully created")

# reserve a port and ip address
port = 80

# bind the port and address that makes server listen to the request
server_socket.bind(('127.0.0.1', port))

# put the socket into listening mode 
server_socket.listen(1)
print("socket is listenning on port 80 ..")

while True:
    # establish a connection with a client 
    client_socket, client_address = server_socket.accept()
    print(f"got connection from {client_address}")
    
    # recieve data from client
    request_data = client_socket.recv(1024).decode("utf-8")
    print(f"request data: \n {request_data}")
    
    #extract request path from request line
    request_line = request_data.splitlines()[0]
    request_path = request_line.split(" ")[1]
    
    # check if the request path is the root ("/")
    if request_path == '/':
        request_path = '/index.html'
    
    # cinstructing the file path by www to the requested path
    file_path = f'www{request_path}'
    
    # check if the file exist and not a directory
    if os.path.exists(file_path) and os.path.isfile(file_path):
        with open(file_path, 'r') as file:
            response_body = file.read()
        response = (
            "HTTP/1.1 200 OK\r\n"
            "Content-Type: text/html; charset=UTF-8\r\n\r\n"
            f"{response_body}"
        )
    else:
        response = (
            "HTTP/1.1 404 Not Found\r\n"
            "Content-Type: text/html; charset=UTF-8\r\n\r\n"
            "<h1>404 Not Found</h1><p>The requested URL was not found on this server.</p>"
        )


    # send the response to the client
    client_socket.sendall(response.encode("utf-8"))

    #close the connection with the client 
    client_socket.close()
    
    
