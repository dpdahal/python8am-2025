# class Bank:
#     __name="SBI"
#     __account=1234567890

#     def getBank(self):
#         return self.__name
    
#     def setBank(self,name):
#         self.__name = name


# obj = Bank()
# obj.setBank("HDFC")
# print(obj.getBank())


class Bank:
    __name="SBI"

    @property
    def name(self):
        return self.__name
    
    @name.setter
    def name(self,name):
        self.__name = name


obj = Bank()
obj.name='test'
print(obj.name)
