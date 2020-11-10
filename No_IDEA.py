def no_idea(l,set_1):
    count = 0
    for i in range(l[0][1]):
        if l[2][i] in set_1:
            count = count + 1
        if l[3][i] in set_1:
            count = count - 1
    return count
    
list_1 = []
for i in range(4):
    User_Data = list(map(int,input().split()))
    list_1.append(User_Data)
n = set(list_1[1])
print(list_1)
result = no_idea(list_1,n)

print(result)
