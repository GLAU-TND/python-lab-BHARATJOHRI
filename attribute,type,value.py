try:
    a = 10
    b = int("bharat")
    c = a + b
    print(c)
except ValueError as e:
    print(e)
try:
    a = 10
    b = "bharat"
    c = a + b
    print(c)
except TypeError as e:
    print(e)

try:
    a = 10
    print(a.count)
except TypeError as e:
    print(e)