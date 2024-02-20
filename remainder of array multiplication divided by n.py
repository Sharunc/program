n = int(input("enter the number"))
a = [12,43,45,23,43,15]
b = []

for i in a:
    c = i % n
    b.append(c)

print(b)