# Web_Server (2024)
## Overview

This project involves creating a basic HTTP web server using Python. The server listens for incoming HTTP requests, processes them, and serves static HTML content from a specified directory. It supports handling multiple concurrent connections and includes basic security measures to prevent unauthorized file access.

## Features

1. Basic HTTP Server Functionality:
   - Port 80 Listening: The server listens for HTTP requests on the default port 80.
   - Concurrent Request Handling: Uses threading to handle multiple client connections simultaneously.

2. Request Handling:
   - GET Requests: Processes HTTP GET requests.
   - Request Path Extraction: Extracts and interprets the requested path from the HTTP request line.
   - Default File Serving: Serves index.html when the root path / is requested.

3. File Serving:
   - Static File Serving: Reads and returns HTML file contents.
   - Content-Type Header: Sends text/html content type in HTTP responses.
   - 404 Handling: Returns a 404 Not Found error for invalid paths or missing files.

4. Concurrency:
   - Threaded Handling: Each request is managed by a new thread, enabling the server to handle multiple connections concurrently.

5. Security:
   - Directory Traversal Protection: Ensures files served are within the specified www directory to prevent unauthorized file access.
   - Customizable Document Root: Allows specifying the www directory at server startup.

6. Logging and Debugging:
   - Request Logging: Logs requested paths and thread IDs.
   - Simulated Processing Time: Introduces a delay to simulate longer processing times for testing concurrency.

## How to Run the Server

1. Save the Code:
   Save the server code into a Python file, e.g., web_server.py.

2. Create www Directory:
   Create a www directory in the same directory as the script (or specify a different path when running the script).

3. Add Content:
   Place an index.html file and any other HTML files you want to serve inside the www directory.

4. Run the Server:
   Open a terminal and run the server
  
