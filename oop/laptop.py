# class Laptop:
#     def brand(self,name):
#         print(f"Brand name is {name}")

# class Dell(Laptop):
#     pass

# class Mac(Laptop):
#     pass

# obj = Dell()
# obj.brand("Dell")
# obj1 = Mac()
# obj1.brand("Mac")

# WAP to create Mobile parent class that 
# includes brand, model, price and child class Samsung and Apple




# class Laptop:
#    def __init__(self,name):
#        print("I am parent class",name)

# class Dell(Laptop):
#     def __init__(self,name):
#         # super().__init__(name)
#         Laptop.__init__(self,name)
#         print("I am child class")



# obj = Dell("Dell")



# class Mobile:

#     @staticmethod
#     def info():
#         print("I am static method")


# Mobile.info()



# class Mobile:
#     x=10

#     @classmethod
#     def info(cls):
#         print(cls.x)



# Mobile.info()