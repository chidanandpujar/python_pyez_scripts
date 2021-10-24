fd = open("check_class1.py", "r")
fd2 = open("check_fileio_test.py","w")


lines = [ "#Script Author : xyz\n" ,"#Script Name : test\n" ]
fd2.writelines(lines)

for line in fd:
    fd2.write(line)
fd.close()
fd2.close()

fd3 = open("check_fileio_test.py", "r")
for lines in fd3:
    print(lines)
