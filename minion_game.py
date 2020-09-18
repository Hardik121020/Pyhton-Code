def minion_game(string):

    list_1 =[]
    for i in range(len(string)):
        for j in range(i+1,len(string)+1):
            list_1.append(string[i:j])

    score = dict()
    for i in list_1:
        if i in score:
            score[i] = score[i] + 1
        else:
            score[i] = 1

    vowels = ['A','E','I','O','U','a','e','i','o','u']
    stuart_score = 0
    kevin_score = 0

    for i in score:
        if i[0] not in vowels and i[0].isalpha:
            stuart_score = stuart_score + score[i]
        elif i[0] in vowels and i[0].isalpha:
            kevin_score = kevin_score + score[i]
        else:
            continue
    
    if stuart_score > kevin_score:
        print("%s %s" %("Stuart",stuart_score))
    elif kevin_score > stuart_score:
        print("%s %s" %("kevin",kevin_score))
    else:
        print("Draw")




if __name__ == '__main__':
    s = input()
    minion_game(s)
