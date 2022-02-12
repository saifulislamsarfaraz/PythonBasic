a = 10
b = 20
c = 60


"""
if a > b:
    if a > c:
        print(a)
    else:
        print(c)
elif b > a:
    if b > c:
        print(b)
    else:
        print(c)
"""


print(a if a > b else b)