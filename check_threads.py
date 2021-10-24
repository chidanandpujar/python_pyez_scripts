import threading

def my_thread_function():
    print("Simple thread execution")

t = threading.Thread(target=my_thread_function())
t.start()

class my_thread_class(threading.Thread):
    def run(self):
        print("Simple thread execution with derived class threading.Thread")

ct1 = my_thread_class()
ct1.start()
ct1.join()
