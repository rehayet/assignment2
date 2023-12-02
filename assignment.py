list = ["ab", "cd","ef"]
liste=[]
for i in list:
    sum = 0
    for j in i:
        sum = sum + ord(j)
    liste.append(sum)    
print(liste)