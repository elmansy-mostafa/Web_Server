
import socket

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
    
    # create the response 
    response = f"HTTP/1.1 200 OK\r\n\r\nRequested path: {request_path}\r\n"

    # send the response to the client
    client_socket.sendall(response.encode("utf-8"))

    #close the connection with the client 
    client_socket.close()
    
    
