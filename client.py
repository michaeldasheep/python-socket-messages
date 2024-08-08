import socket
import threading

# User Set Variables
host = "127.0.0.1"
port = 6000
identity = "Your Name"

def main():
    global host
    global port
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.connect((host, port))
    print(f"Socket Client is connected to Host: {host} and Port: {port}.")
    try:
        while True:
            recieve = threading.Thread(target=receiver, args=(s,))
            send = threading.Thread(target=sender, args=(s,))
            recieve.start()
            send.start()
        s.close()
    except KeyboardInterrupt:
        s.close()
        print("Program Exitting...")
        quit()

def sender(conn):
    global identity
    while True:
        message = input("Enter a message: ")
        if message == "!exit":
            break
        elif message != "":
            data = '{ "code":"1", "identity":"' + identity + '", "msg":"' + message + '"}'
            conn.send(data)

def receiver(conn):
    while True:
        receivedData = conn.recv(1024)
        if not receivedData:
            continue
        else:
            print(receivedData)

if __name__ == "__main__":
    main()