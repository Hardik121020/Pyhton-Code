from itertools import permutations
n = input().split()
k = int(n[1])
L1 = []
for i in n[0]:
    for j in range(len(i)):
        L1.append(i[j])
perm = list(permutations(L1,k))
perm.sort()
for i in perm:
    t = ""
    for j in i:
        t = t + j
    print(t)
