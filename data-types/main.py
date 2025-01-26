# what is data types?
# data types is a category for values, and every value belongs to exactly one data type.


# There are two types of data types in python
# 1. Primitive data types: int, float, complex, bool, str,None
# 2. Non-primitive data types: list, tuple, set, dict, frozenset, bytes, bytearray, range



# x=1034567
# print(type(x))

# x=1034.567
# print(type(x))


# a =True

# a =45+67j
# print(type(a))
# print(a.real)
# print(a.imag)


# course ="python"
# print(type(course))

# a  = None

# price =456.98767811111111111111
# print(f"{price:.2f}")

# a =int(input("Enter a: "))
# b =int(input("Enter b: "))
# print(a+b)

# a ='56'
# print(type(a))
# a =int(a)
# print(type(a))

# name ='sophia'
# print(name[-1])

# a = 65
# print(type(a))
# print(id(a))
# print(dir(a))
# print(ord('B'))
# print(chr(65))


# course ="we are learning python"
# print(course.upper())
# print(course.capitalize())
# print(course.title())
# print(dir(course))
# print(course[2:10])

# first_name
# middle_name
# last_name

# Ram Singh Thapa

# WAP to enter five subject marks and calculate the total marks and percentage
# WAP to enter principle, rate and time and calculate the simple interest

# a =5

# a =[1,2,3.7,4,'ram']


# what is list?
# list is a collection of items in a particular order.
# list is mutable
# list is ordered
# list allows duplicate values
# list is defined by square brackets []
# index starts from 0
# data =['ram','sita','gita','hari','ram']
# print(data[0])


# data =['ram','sita','gita','hari','ram']
# data[0]='laxmi'
# print(data)

# data =[]
# print(dir(data))

# 'append', 'clear', 'copy', 'count', 'extend', 
# 'index', 'insert', 'pop', 'remove', 'reverse', 'sort'

# data=[]
# data.append('ram')
# data.append('sita')
# data.clear()
# print(data)
# data1 =data.copy()
# print(data1)
# print(data)

# data =['ram','sita','gita','hari','rama']
# data.sort(reverse=True)
# print(data)
# data.reverse()
# print(data)
# print(data.remove('ram'))
# print(data.pop(2))
# print(data.count('ram'))

# data =['ram','sita']
# data.insert(0,'gita')
# print(data)
# data1 =['gita','hari']
# data.extend(data1)
# print(data)

# print(data.index('sita'))


# data=[
#     ['ram','sita','gita'],
#     ['hari','rama','sophia'],
# ]
# print(data[1][1])


# What is tuple?
# tuple is a collection of items in a particular order.
# tuple is immutable
# tuple is ordered
# tuple allows duplicate values
# tuple is defined by round brackets ()
# index starts from 0
# data =('ram','sita','gita','hari','ram')
# data[0]='hari'
# print(dir(data))
# print(data[0])

# week_names =('mon','tue','wed','thu','fri','sat','sun')


# What is set?
# set is a collection of items in a particular order.
# set is mutable
# set is unordered
# set unique values
# set is defined by curly brackets {}

# data ={'ram','sita','gita','hari','ram','sita'}
# print(data)

# What is dictionary?
# dictionary is a collection of items in a particular order key value pair.
# dictionary is mutable
# dictionary is unordered
# dictionary unique keys
# dictionary is defined by curly brackets {}


data={
    'name':'ram',
    'age':45,
    'address':'ktm',
    'contact':{
        'phone':984567890,
        'email':'ram.com'
    }
}

# print(data['names'])
# print(data.get("name","Key not found"))
# print("We are learning python data types")
# print(data['contact']['phone'])

# print(data.keys())
# print(data.values())
# print(data.items())


