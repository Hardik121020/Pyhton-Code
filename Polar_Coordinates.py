import cmath
n = input().split()

if (len(n[0]) > 1):
    x = int(n[0][0])
    y = int(n[0][2])
else:
    print("Invalid complex number")
if y != 0:
    Phase = cmath.phase(complex(x,y))
    Distance = abs(complex(x,y))
    print(Distance)
    print(Phase)
else:
    print("Invalid complex number")
