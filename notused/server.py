import _thread
import threading
import socket
import json

sendData = ""
dataSendParam = False
print_lock = threading.Lock()
close = False

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
        while True:
            client, addr = s.accept()
            print(f"New Connection from: {addr[0]}:{addr[1]}.")
            #_thread.start_new_thread(receiver,(client,addr))
            #_thread.start_new_thread(sender,(client,addr))
            recieve = threading.Thread(target=receiver, args=(client,addr))
            send = threading.Thread(target=sender, args=(client,addr))
            recieve.start()
            send.start()
        s.close()
    except KeyboardInterrupt:
        print_lock.acquire()
        s.close()
        close = True
        print("Program Exitting...")
        exit()

def receiver(client,addr):
    cond = True
    print(f"Recieve Handler for {addr[0]}:{addr[1]} started.")
    while cond == True:
        data = client.recv(1024).decode()
        print(data)
        if not data:
            cond = False
        else:
            receiveHandler(data, addr)
    print(f"Receive Handler Thread for {addr[0]}:{addr[1]} has been closed.")
    client.close()

def receiveHandler(data, addr):
    global dataSendParam
    global sendData
    parsed = json.loads(data)
    code = parsed['code']
    if code == "1":
        iden = parsed['identity']
        msg = parsed['msg']
        sendData = "[ '" + iden + "': '" + msg + "' ]"
        print(sendData)
        dataSendParam = True
    elif code == "2":
        print(f"Socket Feed Client Connected on {addr[0]}:{addr[1]}.")
    elif code == "3":
        print(f"Socket Send Client Connected on {addr[0]}:{addr[1]}.")
    elif code == "4":
        print(f"Socket Send and Recieve Client Connected on {addr[0]}:{addr[1]}.")
            
def sender(client,addr):
    global sendData
    global dataSendParam
    cond = True
    print(f"Send Handler for {addr[0]}:{addr[1]} started.")
    while cond == True:
        if dataSendParam == True:
            client.sendall(sendData.encode())
            dataSendParam = False
        keepalive = client.recv(1024).decode()
        if not keepalive:
            cond = False
    print(f"Send Handler Thread for {addr[0]}:{addr[1]} has been closed.")            
    client.close()

if __name__ == "__main__":
    server()