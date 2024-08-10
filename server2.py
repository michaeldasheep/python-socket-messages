import threading
import socket
import json

# Server Settings
Authkey = "none" # Authentication required or not ( plaintext )

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
    global Authkey
    host = "0.0.0.0"
    port = 64000
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.bind((host, port))
    s.listen(5)
    print(f"Socket Server is listening on Host: {host} and Port: {port}.")
    try:
        while True:
            client, addr = s.accept()
            print(f"New Connection from: {addr[0]}:{addr[1]}.")
            data = client.recv(1024).decode()
            if not data:
                continue
            else:
                parsed = json.loads(data)
                code = parsed['code']
                inAuthkey = parsed['authkey']
                if code == "2":
                    inAuthkey = parsed['authkey']
                    if Authkey == inAuthkey:
                        recieve = threading.Thread(target=receiver, args=(client,addr))
                        recieve.start()
                    else:
                        msg = "Auth Key Incorrect"
                        client.sendall(msg.encode())
                        del msg
                        client.close()
                elif code == "3":
                    send = threading.Thread(target=sender, args=(client,addr))
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
    data = client.recv(1024).decode()
    if not data:
        print(f"Receive Handler Thread for {addr[0]}:{addr[1]} has been closed.")
        client.close()
        exit()
    print(f"Recieved Message: {data}.")
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
        dataSendParam = True
            
def sender(client,addr):
    global sendData
    global dataSendParam
    cond = True
    print(f"Send Handler for {addr[0]}:{addr[1]} started.")
    while cond == True:
        if dataSendParam == True:
            client.sendall(sendData.encode())
            dataSendParam = False
            cond = False
    print(f"Send Handler Thread for {addr[0]}:{addr[1]} has been closed.")            
    client.close()

if __name__ == "__main__":
    server()