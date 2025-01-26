# what is filehandle?
# filehandle is a variable that is used to store the file object 
# returned by the open() function.

# mode = 'r' is used to read the file
# mode = 'w' is used to write the file
# mode = 'a' is used to append the file
# mode = 'r+' is used to read and write the file

# types of file
# 1. Text file
# 2. Binary file

# handle = open("record/db.txt", "a")
# handle.write("Hello, update! \n")
# handle.write("Hello, test! \n")
# handle.close()

# name,email,address

# obj = open("record/db.txt", "r")
# # print(obj.read())
# # print(obj.readline())
# print(obj.readlines())


# with open("record/db.txt", "r") as obj:
#     print(obj.read())