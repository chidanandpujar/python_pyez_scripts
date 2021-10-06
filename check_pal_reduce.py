from functools import reduce

if __name__ == "__main__":
    num_list = [1,2,3,4,5,6]
    even_num = list(filter(lambda n:n%2 == 0,num_list))
    print(even_num)
    sum = reduce(lambda a,b: a+b,even_num)
    print(sum)