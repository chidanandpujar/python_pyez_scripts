r = lambda x,y: x + y
print(r(2,3))

print((lambda x,y: x + y)(2,3))

l1 = [ 1,2,3,4,5,6,7,8,9,10]
even_list = list(filter(lambda n:n%2 == 0,l1))
print(even_list)
odd_list = list(filter(lambda n:n%2 !=0,l1))
print(odd_list)
