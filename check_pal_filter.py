def check_pal(str):
    if str == str[::-1]:
        return str;

if __name__ == "__main__":
    str_list = ['bab', 'tot', 'dod', 'cat']
    pals = list(filter(check_pal,str_list))
    print(pals)