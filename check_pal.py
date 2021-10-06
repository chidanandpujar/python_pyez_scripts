
def check_pal(str):
    if str == str[::-1]:
        return str

if __name__ == '__main__':
    str_list = [ 'sat', 'bab', 'cat', 'tot']
    result =map(check_pal,str_list)
    print(list(result))

