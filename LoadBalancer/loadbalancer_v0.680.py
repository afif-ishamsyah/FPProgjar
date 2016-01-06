# FP Progjar B
# Load Balancing v.0.680
# Weighted Round-Robin
# 5113100172 - 5113100173 - 5113100175 - 5113100176 - 5113100180
# Afif I. H. - A. Akram Y. - Naufal B. Fauzan - A. Rafif S. - L. Wismar 
#import mogamogaselesai
import threading
import socket
import time
import sys
import re

data_ip = []
points = 3
point = 0
flags = 0
respo = """HTTP/1.1 302 Found
Location: http://"""

def init_ip():
	data_ip.append('127.0.0.1:3172\n')
	data_ip.append('127.0.0.1:3175\n')
	data_ip.append('127.0.0.1:3176\n')
	data_ip.append('127.0.0.1:3180\n')
	

def count_index():
	global points
	global flags
	point=points
	flag=flags
	if point == 0:
		points = 1
	elif point == 1:
		if flag == 0:
			flags = 1
			points = 0
		elif flag == 1:
			flags = 0
			points = 2
	elif point == 2:
		points = 3
	elif point == 3:
		points = 0
	return points

def get_resp(datas, soker):
	global points
	pointer=count_index()
	responses=''
	if datas:
		responses=respo+data_ip[pointer]
		soker.send(responses)

if __name__ == '__main__':
	init_ip()
	my_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
	server_address = ('127.0.0.1', 3173)
	my_socket.bind(server_address)
	my_socket.listen(100000)
	while(True):
		connection, client_address = my_socket.accept()
		while(True):
			data=connection.recv(2048)
			print data
			match = re.match('GET / HTTP/1', data)
			if match:
				if data:
					get_resp(data, connection)
					connection.close()
			break