from _thread import *
import threading
import socket

print_lock = threading.Lock()

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
            start_new_thread(receiver, (client,))
            start_new_thread(sender, (client,))
        s.close()
    except KeyboardInterrupt:
        s.close()
        print("Program Exitting...")

def receiver(conn):
    while True:
        data = conn.recv(1024)
        if not not data:
            
            
            


if __name__ == "__main__":
    server()


