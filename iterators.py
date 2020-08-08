from itertools import combinations 

n = int(input())
m = input().split()
k = int(input())

count = 0
num = 0
com = list(combinations(m,k))
for i in com:
    if "a" in i:
        num = num + 1
    else:
        count = count + 1
result = float(num)/(count + num)
print("%.3f" % result) 
