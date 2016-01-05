#!/usr/bin/python

import socket, select, string

html = """
HTTP/1.1 200 OK
Connection: Closed\r\n\r\n
<!DOCTYPE html>
<html>
<body style="background-color:black;" >
<center>
    <h1 style="font-family:verdana;color:white;" ><strong>Webserverku</strong></h1>
    <p style="font-family:verdana;color:blue;" >Andi Akram Yusuf - 5113100173</p>
<center>
</body>
</html>\r\n\r\n"""

def gett(sock, data):
    sock.send(html)
    sock.close()
    CONNECTION_LIST.remove(sock)
    return

if __name__ == "__main__":
     
    # List to keep track of socket descriptors
    CONNECTION_LIST = []
    NAME_LIST = []
     
    server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server_socket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
    server_socket.bind(("0.0.0.0", 10000))
    server_socket.listen(1)
 
    # Add server socket to the list
    CONNECTION_LIST.append(server_socket)

    tmp=''
 
    while 1:
        # Get socket list
        read_sockets,write_sockets,error_sockets = select.select(CONNECTION_LIST,[],[])
 
        for sock in read_sockets:
            #New connection
            if sock == server_socket:
                sockfd, addr = server_socket.accept()
                CONNECTION_LIST.append(sockfd)
                print "New client %s, %s" %addr
                 
            #Recieve message
            else:
                try:    
                    data = sock.recv(4069)
                    if data:
                        tmp=tmp+data
                        if '\r\n\r\n' in tmp:
                            print "Sending message to %s, %s" %addr
                            print tmp
                            tmp=''
                            gett(sock, data)
                        else :
                            print "gagal"
                 
                except:
                    sock.close()
                    CONNECTION_LIST.remove(sock)
                    continue
     
    server_socket.close()