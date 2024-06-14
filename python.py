# a = [10, 20, 30, 40, 60, 70]

# b = a[1:6]
# print(b)

a = []
c = []
for i in range(4):
    b = float(input('Enter Number: '))
    a.append(b)
    c.append(b)
print(a)
print(c)
b = set(c)
for i in b:
    if i in a:
        print("Find:" , i)
    else:
        print("Not Find:" , i)

   
