# Enter your code here. Read input from STDIN. Print output to STDOUT
N = list(map(int,input().split()))
list_1 = []
for i in range(N[1]):
    user = list(map(int,input().split()))
    list_1.append(user)
for i in zip(*list_1):
    print(sum(i)/len(i))
