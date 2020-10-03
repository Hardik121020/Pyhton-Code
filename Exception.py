n = int(input())
for i in range(n):
    k = input().split()
    a = k[0]
    b = k[1]
    try:
        print(int(int(a)/int(b)))
    except ZeroDivisionError:
        print("Error Code: integer division or modulo by zero")
    except ValueError as msg:
        print("Error Code:",msg)
