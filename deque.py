import collections 

n = int(input())
de = collections.deque()
for i in  range(n):
    user_input = input()
    command = user_input.split()
    if command[0] == "append":
        de.append(int(command[1]))
    elif command[0] == "appendleft":
        de.appendleft(int(command[1]))
    elif command[0] == "pop":
        de.pop()
    elif command[0] == "popleft":
        de.popleft()
    else:
        continue

for i in de:
    print(i,end=" ")
