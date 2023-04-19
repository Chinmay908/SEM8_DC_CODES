import socket
import threading

host = "192.168.0.11"
port = 9922

client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client.connect((host, port))

print("\nConnected to the server {}".format(host))

def receive_msgs():
    while True:
        try:
            msg = client.recv(1024)
            print(msg.decode("utf-8"))
            print()

        except:
            client.close()
            break

thread = threading.Thread(target=receive_msgs)
thread.start()

while True:
    print()
    message = input()
    client.send(message.encode("utf-8"))


