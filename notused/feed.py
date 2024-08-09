import socket

# User Set Variables
host = "127.0.0.1"
port = 6000

def main():
    global host
    global port
    global s
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.connect((host, port))
    data = '{ "code":"2" }'
    s.sendall(data.encode())
    print(f"Socket Feed Client is connected to Host: {host} and Port: {port}.")
    try:
        while True:
            receivedData = s.recv(1024).decode()
            #data = '{ "code":"1000", "keepalive":True }' # Keepalive Packets
            #s.send(data.encode())
            if not receivedData:
                continue
            else:
                print(receivedData)
        s.close()
    except KeyboardInterrupt:
        s.close()
        print("Program Exitting...")
        exit()

if __name__ == "__main__":
    main()