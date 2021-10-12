def check_pal(str):
    l1 = str.split()
    pal_list = []
    npal_list = []
    for value in l1:
        if value == value[::-1]:
            pal_list.append(value)
        else:
            npal_list.append(value)
    print(pal_list)
    print(npal_list)

if __name__ == "__main__":
    pal_str = "This is dod mod tot bob"
    check_pal(pal_str)
