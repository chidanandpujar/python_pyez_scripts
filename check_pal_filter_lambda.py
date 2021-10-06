if __name__ == "__main__":
    str_list = ['bab', 'tot', 'dod', 'cat', 'ini']
    pals = list(filter(lambda str: str == str[::-1],str_list))
    print(pals)