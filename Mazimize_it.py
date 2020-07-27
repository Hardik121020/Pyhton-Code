from itertools import product
n = input().split(" ")
k = int(n[0])
m = int(n[1])
L1 = []
for i in range(k):
    z = []
    t = 0
    s = input().split()
    for j in s:
        t = int(j)*int(j)
        z.append(t)
    L1.append(z)
L2 = list(product(*L1))

L3 = []
for i in L2:
    sum_1 = 0
    for j in i:
        sum_1 = sum_1 + j
    t = sum_1%m
    L3.append(t)
print(max(L3))
