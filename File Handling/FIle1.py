
f = open("city.txt","r")

print("Display details of all cities")
for i in f:
    print(i)
f.seek(0)
list_1 = []
for i in f:
    list_1.append(i.split())

print("---------------------------------------------------")
print("Display city names with population more than 10Lakhs")
for i in list_1:
    if float(i[1]) > 10:
        print(i[0])
       
print("------------------------------")
print("Display sum of areas of all cities ")
total = 0

for i in list_1:
    total = total + float(i[2])
print(total)
