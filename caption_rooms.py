import collections
N = int(input())
list_1 = list(map(int,input().split()))
dict_1 = collections.Counter(list_1)
for i in dict_1:
    if dict_1[i] == 1:
        print(i)
    else:
        continue
