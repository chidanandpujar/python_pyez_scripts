import threading

def my_test_thread():
    print("simple thread execution")

t = threading.Thread(target=my_test_thread())
t.start()
