import socket

def state_html(state):
    if state == "ON":
        change = "OFF"
    else:
        change = "ON"
    site = "HTTP/1.1\r\nContent-Type: text/html; charset = utf-8\r\n\r\n"
    site += "<html><body> Diode state: " + state + "<br><a href=/" + change + ">Turn " + change + "</a></body></html>"
    return site


server = socket.socket()

try:
    server.bind(('localhost', 8000))
    server.listen(1)
    print("waiting for connection")
    while True:
        connection, client = server.accept()
        get = connection.recv(1024).decode()

        print(get)
        if "/ON" in get:
            with open("diode.txt", "w") as pol:
                pol.write("ON")
        elif "/OFF" in get:
            with open("diode.txt", "w") as pol:
                pol.write("OFF")
        with open("diode.txt", "r") as pol:
            data = state_html(pol.read())
        connection.sendall(data.encode())
        connection.shutdown(socket.SHUT_WR)
except Exception as e:
    print("Error: ", e)

server.close()