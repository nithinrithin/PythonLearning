from socket import socket, AF_INET, SOCK_STREAM

from threading import Thread

def process_client(client):
    while True:
        data = client.recv(50)
        print "client sent :"+ data
        if not data: break;
        data = data.strip()
        client.send(data.upper())
        if 'bye' in data: break
    client.close()

mysocket = socket(AF_INET, SOCK_STREAM)
mysocket.bind(("127.0.0.1",5050))

print "Echo server listining on port 5050\n"
mysocket.listen(1)

try:
    while True:
        (client, addr) = mysocket.accept()
        print "incomming connection"+ `addr`
        Thread(target=process_client, args=(client,)).start()
        print "h",
except:
    mysocket.close()
    client.close()
    