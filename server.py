import socket

s = socket.socket()
host = socket.gethostname()
port = 21345

s.bind((host, port))
s.listen(1)
print("Waiting for connections...")
conn, addr = s.accept()
print("Client has connected")
conn.send("Welcome".encode())
while True:
    msg = input("Enter a message for client: ")
    conn.send(msg.encode())
    print("Message sent...")
    print("Client is typing...")
    message = conn.recv(1024)
    message = message.decode()
    print("Client Message: " + message)
