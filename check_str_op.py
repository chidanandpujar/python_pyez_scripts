str1 = "testing strings ops"
str2 = str1.split()
print(str2)
str3 = str1.replace("testing","checking").split()
print(str3)
print(len(str1))
print(len(str3))
str4="".join(str2)
print(str4)

myDict = { "name": "test1",
           "lastname": "test2"}

print(myDict)
str5 = "".join(myDict.values())
print(str5)
str6 = "".join(myDict.keys())
print(str6)
str7 = str1.split("strings")
print(str7)
