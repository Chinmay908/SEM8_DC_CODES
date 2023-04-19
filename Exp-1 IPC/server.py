import socket

HOST = "127.0.0.1"
PORT = 4698

def send_data(data):
    return str(data).encode('utf-8')

with socket.socket(socket.AF_INET,socket.SOCK_STREAM) as s:
    s.bind((HOST,PORT))
    print("Server binded to host %s and port %d" %(HOST,PORT))
    s.listen()
    conn,address = s.accept()
    with conn:
        print("Connected by:",address)
        data1 = conn.recv(1024)
        data2 = conn.recv(1024)

        a = int(data1.decode("utf-8"))
        b = int(data2.decode("utf-8"))

        print("Data 1 recieved from Client: ",a)
        print("Data 2 recieved from Client: ",b)

        res = a+b
        conn.sendall(send_data(res))
