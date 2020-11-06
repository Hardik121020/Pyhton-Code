f = open("temp.txt","r")

print("Display all product details")
for i in f:
    print(i)
f.seek(0)
list_1 = []
for i in f:
    list_1.append(i.split())

print("---------------------------------------------------")
print("Find average sale of all products")
       
list_2 = []
for i in list_1:
    total = 0
    t = []
    for j in range(1,len(i)):
        total = total + int(i[j])
    t.append(i[0])
    t.append(total)
    list_2.append(t)
for i in list_2:
    print(i[0] + " " +str(i[1]/4))
print("Find product with maximum sales")
t = []
for i in list_2:
    t.append(i[1])
k = max(t)
for i in list_2:
    if k in i:
        print(i)
