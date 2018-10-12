import socket
import json
import sys

host = '127.0.0.1'
port = 5002

soc = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
source = (host, port)

try:
	with open('filmes.json') as f:
		data_json = json.load(f)
	lista = json.dumps(data_json, ensure_ascii=False, indent=2)
except Exception as erro:
	print("Ocorreu um erro ao carregar o arquivo:")
	print(erro)

try:
	soc.bind(source)
	soc.listen(1)

	print("TCP waiting for connection in port %s"%port)

	c, adress = soc.accept()
	print("Connection from: "+ str(adress))
	
	while True:
		data = c.recv(2048)
		print("from connect user: "+data)
		#print("Sending: "+data)
		#c.send(data.encode('utf-8'))
		if data[:-1] == 'exit server':
			print("Server Disconnected")
			c.close()
		if data[:-1] == 'filmes':
			c.send(lista.encode('utf-8'))

	c.close()
	        
except Exception as erro:
	print erro
	soc.close()