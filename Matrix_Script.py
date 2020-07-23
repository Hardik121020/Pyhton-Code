# Using if else and elif Statement
M = input().split()
row = int(M[0])
col = int(M[1])
List_1 = []

for i in range(row):
    userInput = input()
    if len(userInput) == col:
        List_1.append(userInput)

k = ""

for j in range(col):
    for i in range(row):
        k = k + List_1[i][j]

t = ""
for i in range(len(k)):
    #print(i)
    if k[i].isupper():
        t = t + k[i]
    elif k[i].islower():
        t = t + k[i]
    else:
        count = 0
        for j in range(i,len(k)-i):
            if k[j].isupper():
                count = count + 1
                continue
            elif k[j].islower():
                count = count + 1
                continue
        if count == 0:
            t = t + k[i]
        elif count > 0:
            t = t + " "
k = ""
for i in range(len(t)):
    
    count = 0
    for j in range(i,len(t)-i):
        if t[j].isupper():
            count = count + 1
        elif t[j].islower():
            count = count + 1
            
    if t[i].isupper():
        k = k + t[i]
    elif t[i].islower():
        k = k + t[i]
    elif t[i] == " " and count > 0:
        if t[i+1] != " ":
            k = k + " "
        else:
            continue
    elif count == 0:
        k = k + t[i]
    
print(k)
