from _thread import *
import threading
import socket
import json

sendData = ""
dataSendParam = False
print_lock = threading.Lock()

def t_print(*a, **b):
    """Thread safe print function"""
    with print_lock:
        print(*a, **b)

def server():
    global s
    global client
    host = "0.0.0.0"
    port = 6000
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.bind((host, port))
    s.listen(5)
    print(f"Socket Server is listening on Host: {host} and Port: {port}.")
    try:
        client, addr = s.accept()
        #print_lock.acquire()
        print(f"New Connection from: {addr[0]}:{addr[1]}.")
        recieve = threading.Thread(target=receiver)
        send = threading.Thread(target=sender)
        recieve.start()
        send.start()
    except KeyboardInterrupt:
        s.close()
        print("Program Exitting...")
        exit()

def receiver():
    global s
    global client
    global sendData
    global dataSendParam
    while True:
        data = client.recv(1024).decode()
        parsed = json.loads(data)
        code = parsed['code']
        if code == "1":
            iden = parsed['identity']
            msg = parsed['msg']
            sendData = "[ " + iden + ": " + msg + " ]"
            dataSendParam = True

            
def sender():
    global s
    global client
    global sendData
    global dataSendParam
    while True:
        if dataSendParam == True:
            client.send(sendData.encode())
            dataSendParam = False

if __name__ == "__main__":
    server()


