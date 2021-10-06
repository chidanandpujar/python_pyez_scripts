def check_dod(str):
    if str ==  'dod':
        return str
    else:
        return "NotFound"


if __name__ == "__main__":
    str_list = ['bab', 'tot', 'dod', 'cat', 'ini']
    pals = list(filter(lambda str: str == str[::-1],str_list))
    print(pals)

    check_dod = list(map(check_dod,pals))
    print(check_dod)