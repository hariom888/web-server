import socket 
import time 

server_host = "0.0.0.0"
server_port=8080
server_socket=socket.socket(socket.AF_INET , socket.SOCK_STREAM) # initliazing the server socket
server_socket.setsockopt(socket.SOL_SOCKET , socket.SO_REUSEADDR , 1) #allows socket to resuse the local address after the socket is closed.
server_socket.bind(("0.0.0.0" , 8080)) #bind the sever to our ip address 
server_socket.listen(5) #max no of fully established conncetions that can wait in a queue


print(f"listening on port {server_port} ...")
while True:
    client_socket , client_address = server_socket.accept()
    request=client_socket.recv(1500).decode()
    print(request)
    headers = request.split('\n')
    print(headers[0])
    first_header_components = headers[0].split()


    http_method = first_header_components[0]
    path = first_header_components[1]

    if path == '/' :
        fin=open('index.html')
        content = fin.read()
        fin.close()



        response = 'HTTP/1.1 200 OK \n\n' + content 

        client_socket.sendall(response.encode())
        client_socket.close()
        


#this is somehow we create a web sever . 



















        























