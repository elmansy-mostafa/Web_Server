
import socket
import os
import threading
import time
import sys
def handle_request(client_socket, www_dir):
    try:
        # recieve data from client
        request_data = client_socket.recv(1024).decode("utf-8")
        print(f"request data: \n {request_data}")
        
        #extract request path from request line
        request_line = request_data.splitlines()[0]
        request_path = request_line.split(" ")[1]
        
        # check if the request path is the root ("/")
        if request_path == '/':
            request_path = '/index.html'
        
        # construct the absolute file path
        file_path = os.path.abspath(www_dir + request_path)
        
        #ensure the file path is within the www directory
        if not file_path.startswith(os.path.abspath(www_dir)):
            raise FileNotFoundError
        
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
            raise FileNotFoundError
        
    except (FileNotFoundError, IndexError):
        response = (
            "HTTP/1.1 404 Not Found\r\n"
            "Content-Type: text/html; charset=UTF-8\r\n\r\n"
            "<h1>404 Not Found</h1><p>The requested URL was not found on this server.</p>"
        )
        
    # log the thread id and add a delay for testing concurrency
    print(f"Path: {request_path}, Thread Id: {threading.get_ident()}")
    time.sleep(10)  # Add a delay to simulate a long processing time

    # send the response to the client
    client_socket.sendall(response.encode("utf-8"))

    #close the connection with the client 
    client_socket.close()
    

def start_server(www_dir):
    # create a socket object 
    server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    print("socket successfully created")

    # reserve a port and ip address
    port = 80

    # bind the port and address that makes server listen to the request
    server_socket.bind(('127.0.0.1', port))

    # put the socket into listening mode 
    server_socket.listen(5)
    print(f"socket is listenning on port 80 and serving files from {www_dir}")

    while True:
        # establish a connection with a client 
        client_socket, client_address = server_socket.accept()
        print(f"got connection from {client_address}")
        
        #creating a new thread to handle the client request
        client_thread = threading.Thread(target=handle_request, args=(client_socket, www_dir))
        client_thread.start()
        
if __name__ == "__main__":
    if len(sys.argv) != 2 :
        print(f"Usage: {sys.argv[0]} <www_directory>")
        sys.exit(1)
    www_directory = sys.argv[1]
    
    if not os.path.isdir(www_directory):
        print(f"Error: {www_directory} is not a valid directory")
        sys.exit(1)
        
    start_server(www_directory)

    
    
    
    
