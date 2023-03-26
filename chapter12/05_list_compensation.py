a = [3,6,7,8,9,2,4,23,75,23,123,67]

'''for items in a :
    if items%2==0:
        b.append(items)

print(b)'''

#shortcut for above program
b = [items for items in a if items%2==0]
print(b)

#for set 
a = [1,4,2,4,1,2,3]
s = {items for items in a}
print(s)
