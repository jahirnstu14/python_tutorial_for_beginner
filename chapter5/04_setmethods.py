
c={}
print(type(c))

d=set()
print(type(d))
d.add(3)
d.add(3)
d.add(410)
d.add((40,34,34,67)) #list and dict cannot add set but tuple canbe used because it dont change .
print(d)
print(len(d))
d.remove(40)
print(d)

