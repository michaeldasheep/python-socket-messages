from _thread import *
import threading
import socket
import json

print_lock = threading.Lock()
sendData = ""
dataSendParam = False

def server():
    host = "0.0.0.0"
    port = 6000
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.bind((host, port))
    s.listen(5)
    print(f"Socket Server is listening on Host: {host} and Port: {port}.")
    try:
        while True:
            client, addr = s.accept()
            #print_lock.acquire()
            print(f"New Connection from: {addr[0]}:{addr[1]}.")
            recieve = threading.Thread(target=receiver, args=(client,))
            send = threading.Thread(target=sender, args=(client,))
            recieve.start()
            send.start()
        s.close()
    except KeyboardInterrupt:
        s.close()
        print("Program Exitting...")
        quit()

def receiver(conn):
    global sendData
    global dataSendParam
    while True:
        data = conn.recv(1024)
        parsed = json.loads(data)
        if parsed['code'] == "1":
            iden = parsed['identity']
            msg = parsed['msg']
            sendData = iden, ": ", msg
            dataSendParam = True

            
def sender(conn):
    global sendData
    global dataSendParam
    while True:
        if dataSendParam == True:
            conn.send(sendData)
            dataSendParam = False

if __name__ == "__main__":
    server()


