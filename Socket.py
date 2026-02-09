import socket
s=socket.socket()
print("Socket created")
port=123
host=socket.gethostname()
s.bind((host,port))
print("Socket bind to",port)
s.listen(3)
print("Socket now listening....")

while True:
    c,addr=s.accept()
    print("Connected to",addr)
    c.send(b"Thankyou for connecting")
    c.close()