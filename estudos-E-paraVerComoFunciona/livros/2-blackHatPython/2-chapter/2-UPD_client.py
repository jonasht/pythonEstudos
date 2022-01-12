import socket

# target_host = '127.0.0.1'
# endereço da google br
# target_host = '172.217.162.99'
target_host = 'www.google.com.br'

target_port = 9997


# criando objeto
client = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

# enviando dados
client.sendto(b'AAABBBCCC', (target_host, target_port))

# recebendo dados
data, addr = client.recvfrom(4096)

print('dados:')
print(data.decode())
client.close()
