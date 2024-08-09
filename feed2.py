import socket

# User Set Variables
host = "127.0.0.1"
port = 64000

def main():
    global host
    global port
    global s
    print(f"Socket Feed Client is connected to Host: {host} and Port: {port}.")
    try:
        while True:
            s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            s.connect((host, port))
            start = '{ "code":"3","dumb":"True"}'
            s.sendall(start.encode())
            receivedData = s.recv(1024).decode()
            s.close()
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