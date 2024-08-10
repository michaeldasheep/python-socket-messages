from os import system, name 
import socket

# User Set Variables
host = "110.232.114.228"
port = 64000

def main():
    global host
    global port
    global s
    clear()
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

def clear(): 
    # for windows 
    if name == 'nt': 
        _ = system('cls') 
    # for mac and linux(here, os.name is 'posix') 
    else: 
        _ = system('clear') 

if __name__ == "__main__":
    main()