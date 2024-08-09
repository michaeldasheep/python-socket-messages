import socket
import threading
import time

# User Set Variables
host = "127.0.0.1"
port = 6000
identity = "Your Name"


print_lock = threading.Lock()
close = False

def t_print(*a, **b):
    """Thread safe print function"""
    with print_lock:
        print(*a, **b)

def main():
    global host
    global port
    global s
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.connect((host, port))
    data = '{ "code":"4" }'
    s.sendall(data.encode())
    print(f"Socket Client is connected to Host: {host} and Port: {port}.")
    try:
        recieve = threading.Thread(target=receiver)
        send = threading.Thread(target=sender)
        recieve.start()
        send.start()
    except KeyboardInterrupt:
        s.close()
        print("Program Exitting...")
        exit()

def sender():
    global identity
    global s
    global close
    while True:
        time.sleep(1)
        print_lock.acquire()
        message = input("Enter a message: ")
        print_lock.release()
        if message == "!exit":
            s.close()
            close = True
            exit()
        elif message != "":
            data = '{ "code":"1", "identity":"' + identity + '", "msg":"' + message + '"}'
            s.sendall(data.encode())

def receiver():
    global s
    global close
    while True:
        receivedData = s.recv(1024).decode()
        if not receivedData:
            continue
        else:
            print_lock.acquire()
            print(receivedData)
            print_lock.release()
        if close == True:
            s.close()
            exit()

if __name__ == "__main__":
    main()