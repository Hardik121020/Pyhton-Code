string = input()
count = 1
string = string + " "
for i in range(len(string)-1):
    k = ()
    L1 = list(k)
    if string[i] == string[i+1]:
        count = count + 1
    elif string[i] != string[i+1]:
        L1.append(count)
        L1.append(int(string[i]))
        k = tuple(L1)
        print(k, end = " ")
        count = 1 
