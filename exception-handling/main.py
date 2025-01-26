try:
    print(10/2)
except Exception as e:
    print("Error: ", e)
finally:
    print("Finally block is executed")
print("we are learning exception handling")


def add(x,y):
    if y==0:
        raise Exception("y should not be zero")
    return x/y


try:
    print(add(10,0))
except Exception as e:
    print("Error: ", e)
