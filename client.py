import socket
import threading
import time

# User Set Variables
host = "127.0.0.1"
port = 6000
identity = "Your Name"


print_lock = threading.Lock()

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
    while True:
        time.sleep(1)
        print_lock.acquire()
        message = input("Enter a message: ")
        print_lock.release()
        if message == "!exit":
            s.close()
            exit()
        elif message != "":
            data = '{ "code":"1", "identity":"' + identity + '", "msg":"' + message + '"}'
            s.send(data.encode())

def receiver():
    global s
    while True:
        receivedData = s.recv(1024).decode()
        if not receivedData:
            continue
        else:
            print_lock.acquire()
            print(receivedData)
            print_lock.release()

if __name__ == "__main__":
    main()