import threading
import time

def one():
    time.sleep(5)
    print("One")
    return "one"

def two():
    print("Two")
    return "two"

if __name__ == "__main__":
    one = threading.Thread(target=one, args=())
    two = threading.Thread(target=two, args=())
    one.start()
    two.start()

    