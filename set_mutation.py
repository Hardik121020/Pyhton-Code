N = int(input())
list_1 = list(map(int,input().split()))
M = int(input())
set_1 = set(list_1)
for i in range(M):
    list_2 = []
    command = input().split()
    set_2 = list_2 = list(map(int,input().split()))
    set(list_2)
    if command[0] == "intersection_update":
        set_1.intersection_update(set_2)
    elif command[0] == "update":
        set_1.update(set_2)
    elif command[0] == "symmetric_difference_update":
        set_1.symmetric_difference_update(set_2)
    elif command[0] == "difference_update":
        set_1.difference_update(set_2)
print(sum(set_1))
