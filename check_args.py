def my_func(*args):
    t=0
    for value in args:
        t=t+value
    print(t)

if __name__ == "__main__":
    my_func(1,2,3)
    my_func(1,2,3,4,5)
    my_func(1,2,3,4,5,6)
