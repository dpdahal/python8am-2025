# data =['ram','sita','gita','laxmi']
# # for name in data:
# #     print(name)
# users=[
#     {'username':'admin','password':'admin'},
#     {'username':'ram','password':'ram'},
# ]
# # for user in users:
# #     print(user['username'])
# for x in range(1,11):
#     print(x)
# numbers=[
#     [1,2,3,4,5],
#     [6,7,8,9,10],
#     [11,12,13,14,15]
# ]


# data =['ram','sita','gita','laxmi']

# x=0

# while x<len(data):
#     print(data[x])
#     x+=1

# students=[]
# num =int(input("Enter number of students: "))
# x=1
# while x<=num:
#     name =input(f"Enter name of student {x}: ")
#     students.append(name)
#     x+=1

# print(students)

# 1,10


# students=[
#     {'name':'ram','gender':'male','status':True},
#     {'name':'sita','gender':'female','status':True},
#     {'name':'gita','gender':'female','status':False},
#     {'name':'gopal','gender':'male','status':False},
# ]

# total_user
# total_active_user
# total_inactive_user
# total_active_male_user
# total_active_female_user
# total_inactive_male_user
# total_inactive_female_user


# num = int(input("Enter number of students: "))
# students_marks=[]
# start =1
# while start<=num:
#     print(f"==============Student {start}==============")
#     nep =int(input("Enter nepali marks: "))
#     eng =int(input("Enter english marks: "))
#     math =int(input("Enter math marks: "))
#     sci =int(input("Enter science marks: "))
#     soc =int(input("Enter social marks: "))
#     total =nep+eng+math+sci+soc
#     students_marks.append(total)

#     start+=1
# print("Sn\tTotal Marks\tPercentage\tGrade")
# x=1
# for mark in students_marks:
#     per =mark/5
#     grade =""
#     if per>=80:
#         grade="Grade A"
#     elif per>=60:
#         grade="Grade B"
#     elif per>=40:
#         grade="Grade C"
#     else:
#         grade="Grade D"
    
#     print(f"{x}\t{mark}\t \t{per}\t \t{grade} \n")
#     x+=1
    



# category =[
#     {'cid':1,'name':'Electronics'},
#     {'cid':2,'name':'Clothing'},
#     {'cid':3,'name':'Grocery'},
# ]


# products=[
#     {'pid':1,'name':'Mobile','price':20000,'quantity':2,'cid':1},
#     {'pid':2,'name':'Laptop','price':50000,'quantity':1,'cid':1},
#     {'pid':3,'name':'T-shirt','price':500,'quantity':3,'cid':2},
#     {'pid':4,'name':'Jeans','price':1500,'quantity':2,'cid':2},
#     {'pid':5,'name':'Rice','price':50,'quantity':5,'cid':3},
#     {'pid':6,'name':'Dal','price':100,'quantity':2,'cid':3},
# ]

# name = input(f"Enter the category name: ")
# for cat in category:
#     if cat['name']==name:
#         for product in products:
#             if product['cid']==cat['cid']:
#                 total = product['price'] * product['quantity']
#                 print(f"Product Name: {product['name']} Price: {product['price']}  Quantity: {product['quantity']}  Total: {total}")
    

# users=[
#     {'username':'admin','password':'admin'},
#     {'username':'ram','password':'ram'},
# ]

# products=[
#     {'pid':1,'name':'Mobile','price':20000,'quantity':2,'cid':1},
#     {'pid':2,'name':'Laptop','price':50000,'quantity':1,'cid':1},
#     {'pid':3,'name':'T-shirt','price':500,'quantity':3,'cid':2},
#     {'pid':4,'name':'Jeans','price':1500,'quantity':2,'cid':2},
#     {'pid':5,'name':'Rice','price':50,'quantity':5,'cid':3},
#     {'pid':6,'name':'Dal','price':100,'quantity':2,'cid':3},
# ]


# faculty=[
#     {'fid':1,'name':'Science'},
#     {'fid':2,'name':'Management'},
#     {'fid':3,'name':'Humanities'},
# ]


# students =[
#     {'sid':1,'name':'ram','fid':1},
#     {'sid':2,'name':'sita','fid':2},
#     {'sid':3,'name':'gita','fid':3},
#     {'sid':4,'name':'gopal','fid':1},
#     {'sid':5,'name':'hari','fid':2},
#     {'sid':6,'name':'nabin','fid':3},
#     {'sid':7,'name':'sabin','fid':1},
#     {'sid':8,'name':'abinash','fid':2},
#     {'sid':9,'name':'anil','fid':3},
#     {'sid':10,'name':'santosh','fid':1},
# ]

# science total?: ram sita