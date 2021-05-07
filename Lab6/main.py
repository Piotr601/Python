import socket

WWWADRESS = "eportal.pwr.edu.pl"
PORT = 80

with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as client:
    client.connect((WWWADRESS, PORT))
    client.sendall(b"GET / HTTP/1.1\r\nHost: eportal.pwr.edu.pl \r\n Accept: text/html\r\n\r\n")
    data = str(client.recv(4096), 'utf-8')
    client.close()

    plik = open("data.txt", "w")
    plik.write(data)
    plik.close

    print(data)
