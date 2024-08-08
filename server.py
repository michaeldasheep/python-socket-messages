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
        mloop()
    except KeyboardInterrupt:
        s.close()
        print("Program Exitting...")

def mloop():
    global print_lock
    while True:
        client, addr = s.accept()
        print_lock.acquire()
        print(f"New Connection from: {addr[0]}:{addr[1]}.")
        start_new_thread(chat, (client,))
    s.close()

def chat(c):
    while True:
        data = c.recv(1024)
        if not data:
            print(f"Connection {client} Dropped")
            print_lock.release()
            break


if __name__ == "__main__":
    server()


