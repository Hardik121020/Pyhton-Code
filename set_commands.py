n = int(input())
s = set(map(int, input().split()))
m = int(input())
for i in range(m):
    Command = input().split()
    if len(Command) == 2 :
        if Command[0] == "remove":
            s.remove(int(Command[1]))
        elif Command[0] == "discard":
            s.discard(int(Command[1]))
        else:
            continue
    elif len(Command) == 1:
        s.pop()
    else:
        continue
print(sum(s))
