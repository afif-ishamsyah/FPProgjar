import threading
import socket
import time
import sys
import re

html = """ 
<!DOCTYPE html>
<html>
<head>
	<title>Webserver | Lino</title>
</head>
<body style="background-color: #00c0ff ">
	<center>
		<h1 style="color: white"><strong>Webserver</strong></h1>
		<p style="color: white">Selamat Datang</p>
	<center>
</body>
</html>"""

class MemprosesClient(threading.Thread):
	def __init__(self,client_socket,client_address,nama):
		self.client_socket = client_socket
		self.client_address = client_address
		self.nama = nama
		threading.Thread.__init__(self)

	def run(self):
		message = ''
		while True:
			data = self.client_socket.recv(40960)
			if data:
				message = message + data #collect seluruh data yang diterima
				print data
				if(data):
					self.client_socket.sendall(html)
					break	
			else:
				break
		self.client_socket.close()

class Server(threading.Thread):
	def __init__(self):
		self.my_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
		self.server_address = ('0.0.0.0',8844)
		self.my_socket.bind(self.server_address)
		threading.Thread.__init__(self)
		print "Webserver berhasil"
	
	def run(self):
		self.my_socket.listen(1)
		nomor=0
		while (True):
			self.client_socket, self.client_address = self.my_socket.accept()
			nomor=nomor+1
			#---- menghandle message cari client (Memproses client)
			my_client = MemprosesClient(self.client_socket, self.client_address, 'PROSES NOMOR '+str(nomor))
			my_client.start()
			#----

serverku = Server()
serverku.start()
