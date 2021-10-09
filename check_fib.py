def check_fib(n):
    a,b=0,1
    while(b<=n):
        print(b);
        a,b=b,a+b


if __name__ == "__main__":
    n = int(input("Entert the Fibonacci range:"))
    check_fib(n)