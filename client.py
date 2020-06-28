import socket

s = socket.socket()
host = socket.gethostname()
port = 21345

s.connect((host, port))
message = s.recv(1024)
message = message.decode()
print("Server Message: " + message)

while True:
    print("Server is typing...")
    message = s.recv(1024)
    message = message.decode()
    print("Server Message: " + message)
    message = input("Enter a Message for Server: ")
    s.send(message.encode())
    print("Message sent...")
