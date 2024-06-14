# x = [[1, 2], [3,4],[5,6]]
# for i in x:
#     # print(i)
#     for j in i:
#         print(j)

x = ["ab" , "cd" , "ef"]
y = []
for i in x:
    sum = 0
    for j in i: 
        sum = sum + ord(j)
    y.append(sum)
print(y)
# sum2 = 0
# for k in y:
#     sum2 = sum2 + k
# print(sum2)


  