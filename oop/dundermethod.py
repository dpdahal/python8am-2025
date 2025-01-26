# class Laptop:

#     def __new__(cls,*args,**kwargs):
#         print("I am new method")
#         return super().__new__(cls)
        
#     def __init__(self,name):
#         print("Laptop object created",name)

#     def info(self):
#         print("This is a laptop info method")

#     def __del__(self):
#         print("Laptop object destroyed")



# obj = Laptop('dell')
# obj.info()


# class Students:
#     name ='admin'

#     def __str__(self):
#         return self.name


# obj = Students()
# print(obj)


# class Students:
#     total =0
#     def __init__(self,name):
#         Students.total +=1


# obj1=Students('admin')
# obj2=Students('ram')
# obj3=Students('sita')
# print(obj1.total)


# class Laptop:
#     pass

# obj = Laptop()
# obj.name = 'dell'
# obj.price = 50000

# print(obj.name)
# print(obj.price)


# class Bank:
#     __name ="SBI"

#     def info(self):
#         print(f"Bank name is {self.__name}")


# obj = Bank()
# # print(obj.__name)
# obj.info()