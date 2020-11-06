Test_Cases = int(input())
for i in range(Test_Cases):
    t = []
    Size_A = int(input())
    A = set(list(map(int,input().split())))
    Size_B = int(input())
    B = set(list(map(int,input().split())))
    
    for j in A:
        if j not in B:
            print("False")
            break
    else:
        print("True")
    
