def printargs(**kwargs):
    print(kwargs)


if __name__ == "__main__":
    printargs(a="1",b="2",c="3")
    printargs(ssh=22,ftp=23,dns=53)
