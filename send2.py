import socket
import time

# User Set Variables
host = "127.0.0.1"
port = 64000
identity = "Michael Test"

def main():
    print(f"Socket Send Client is connected to Host: {host} and Port: {port}.")
    try:
        sender()
        s.close()
    except KeyboardInterrupt:
        s.close()
        print("Program Exitting...")
        exit()

def sender():
    global identity
    global s
    global host
    global port
    while True:
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        s.connect((host, port))
        start = '{"code":"2","dumb":"True"}'
        s.sendall(start.encode())
        message = input("Enter a message: ")
        if message == "!exit":
            s.close()
            exit()
        elif message != "":
            data = '{ "code":"1", "identity":"' + identity + '", "msg":"' + message + '" }'
            s.sendall(data.encode())
            s.close()

if __name__ == "__main__":
    main()