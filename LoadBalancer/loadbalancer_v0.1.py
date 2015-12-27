# FP Progjar B
# Load Balancing v.0.100
# Unweighted Round-Robin
# 5113100172 - 5113100173 - 5113100175 - 5113100176 - 5113100180
# Afif I. H. - A. Akram Y. - Naufal B. Fauzan - A. Rafif S. - L. Wismar 
import threading
import socket
import time
import sys

data_ip = []
data_port = []
points = 1 #mulai dari akhir
point = 0
serv_0 = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
serv_1 = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

def init_ip():
	data_ip.append('127.0.0.1')
	data_ip.append('127.0.0.1')
	data_port.append(3172)
	data_port.append(3173)

def init_so():
	serv_0.connect((data_ip[0], data_port[0]))
	serv_1.connect((data_ip[1], data_port[1]))

def count_index():
	global points	
	point=points
	if point == 0:
		points = 1
	elif point == 1:
		points = 0
	return points

def get_resp(datas, soker):
	global points
	pointer=count_index()
	responses=''
	if datas:
		if pointer==0:
			responses=serv_0.recv(2048)
		elif pointer==1:
			responses=serv_1.recv(2048)
		soker.send(responses)

class balancing(threading.Thread):
	def __init__(self, connection, client_address):
		self.connection=connection
		self.client_address=client_address
		threading.Thread.__init__(self)
	
	def run(self):
		data = ""
		if True:
			data=self.connection.recv(2048)
			if data:
				get_resp(data, self.connection)
			self.connection.close()
				
class loading(threading.Thread):
	def __init__(self):
		self.my_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
		self.server_address = ('127.0.0.1', 3120)
		self.my_socket.bind(self.server_address)
		threading.Thread.__init__(self)
	
	def run(self):
		self.my_socket.listen(100)
		while(True):
			self.client_socket, self.client_address = self.my_socket.accept()
			processes = balancing(self.client_socket, self.client_address)
			processes.start()

if __name__ == '__main__':
	init_ip()
	init_so()
	loudb = loading()
	loudb.start()
