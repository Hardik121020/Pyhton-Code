import collections
f = open("movie.txt","r")

print("Count number of movies in the file")
list_1 = []
for i in f:
    list_1.append(i.split())
print(len(list_1))
f.close()

print("Add a new movie detail (War Amit 180 2019) at the end of file.")
f = open("movie.txt","a")
f.write("\nWar Amit 180 2019")
f.close()

print("Display details of all movies where production cost is more than 80 Crores")
f = open("movie.txt","r")

list_1 = []
for i in f:
    list_1.append(i.split())
t = []
for i in list_1:
    t.append(int(2))
print(list_1)

for i in list_1:
    if int(i[2]) > 80:
        print(i)
        
print("Display first five movie details.")
for i in range(5):
    print(list_1[i])
print("Display director name who has worked in more than two movies.")
t = []
for i in list_1:
    t.append(i[1])
k = collections.Counter(t)
print(k)
for i in k:
    if k[i] > 1:
        print(i)
