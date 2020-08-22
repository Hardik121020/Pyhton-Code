list_1 =[]
if __name__ == '__main__':
    n = int(input())
    student_marks = {}
    for _ in range(n):
        name, *line = input().split()
        scores = list(map(float, line))
        student_marks[name] = scores
    query_name = input()
    list_1 = student_marks[query_name]
    total = 0
    for i in list_1:
        total = total + i
    average_marks = (total)/(len(list_1))
    print(format(average_marks,'.2f'))  
