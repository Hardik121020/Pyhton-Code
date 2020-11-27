class Dog:
    def __init__(self,name):
        self.name = name
        self.tricks = []
    def add_trick(self,trick):
        self.tricks.append(trick)

d = Dog("Fido")
e = Dog("Buddy")
e.add_trick("Play Dead")
d.add_trick("roll over")
print(e.tricks)
print(d.tricks)
