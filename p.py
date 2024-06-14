list = ["2m", "td", "abd"]
liste = []
for i in list:
    sum = 0
    for j in i:
        sum = sum + ord(j)
    liste.append(sum)
print(liste)


x = 7000

y = (1+1/x)**x

print(y)