from os import system, name 
import socket

# User Set Variables
host = "110.232.114.228"
port = 64000
identity = "Michael Test"
authkey = "none"

def main():
    clear()
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
    global authkey
    prevMessageSent = False
    while True:
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        s.connect((host, port))
        start = '{"code":"2","authkey":"' + authkey + '"}'
        s.sendall(start.encode())
        print(f"Socket Send Client is connected to Host: {host} and Port: {port}.")
        if prevMessageSent == True:
            print(f"Previous Message '{message}' was successfully sent!")
        message = input("Enter a message: ")
        clear()
        if message == "!exit":
            s.close()
            exit()
        elif message == "!change":
            s.close()
            print("Changing Server")
            host = input("Type in the Host of the new server: ")
            port = int(input("Type in the Port of the new server: "))
            authkey = input("Type in the Authkey of the new server (type nothing if none configured): ")
            print("New Server Details successfully saved!")
        elif message != "":
            data = '{ "code":"1", "identity":"' + identity + '", "msg":"' + message + '" }'
            s.sendall(data.encode())
            prevMessageSent = True
            s.close()

def clear(): 
    # for windows 
    if name == 'nt': 
        _ = system('cls') 
    # for mac and linux(here, os.name is 'posix') 
    else: 
        _ = system('clear') 

if __name__ == "__main__":
    main()