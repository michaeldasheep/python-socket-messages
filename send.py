import socket

# User Set Variables
host = "127.0.0.1"
port = 6000
identity = "Your Name"

def main():
    global host
    global port
    global s
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.connect((host, port))
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
    while True:
        message = input("Enter a message: ")
        if message == "!exit":
            s.close()
            exit()
        elif message != "":
            data = '{ "code":"1", "identity":"' + identity + '", "msg":"' + message + '"}'
            s.send(data.encode())

if __name__ == "__main__":
    main()