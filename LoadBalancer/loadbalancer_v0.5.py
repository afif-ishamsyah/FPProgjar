# FP Progjar B
# Load Balancing v.0.100
# Unweighted Round-Robin
# 5113100172 - 5113100173 - 5113100175 - 5113100176 - 5113100180
# Afif I. H. - A. Akram Y. - Naufal B. Fauzan - A. Rafif S. - L. Wismar 
#import mogamogaselesai
import threading
import socket
import time
import sys
import re

data_ip = []
data_port = []
points = 1
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
	print pointer
	responses=''
	if datas:
		if pointer==0:
			responses=serv_0.recv(2048)
		elif pointer==1:
			responses=serv_1.recv(2048)
		soker.send(responses)

if __name__ == '__main__':
	init_ip()
	init_so()
	my_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
	server_address = ('127.0.0.1', 3133)
	my_socket.bind(server_address)
	my_socket.listen(1)
	while(True):
		connection, client_address = my_socket.accept()
		while(True):
			data=connection.recv(1024)
			print data
			match = re.match('GET / HTTP/1', data)
			if match:
				if data:
					get_resp(data, connection)
					connection.close()
			break
