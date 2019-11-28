def xyz(a,b):
    c = a + b
    if c < 150:
        raise TypeError("Custom Exception Occurred")
    else:
       return c
class MyException(Exception):
    def __init__(self,v):
        self.v = v
        def __str__(self):
            return self.v

a = int(input("Enter the number"))
b = int(input("Enter the number"))
print(xyz(a,b))