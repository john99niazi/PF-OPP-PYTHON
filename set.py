#set random number
'''a={9,1,5,7}
print(a)'''

# type and length
'''a={1,1,2,3,4}
print(a)
print(type(a))
print(len(a))'''

#add the elemnt
'''a={1,3,5,11,7,2}
a.add(8)
a.add(7)
print(a)'''

# upadte funcation
'''a={1,22,33,11,3}
a.update([8,12,99])
print(a)'''

#remove element
'''a={1,2,3,4,56}
a.remove(56)
print(a)'''

#dicard value
'''a={1,2,3,44,23}
a.discard(4)
print(a)'''


#pop funcation
'''a={1,2,3,4,23}
a.pop()
print(a)'''


#delte set
'''a={1,2,3,4}
del a
print(a)'''

#for each loop
'''a={1,2,3,4}
for e in a:
    print(e)'''

#15 not in a
'''a={1,2,3,4}
print(15 not in a)
print(1 in a)
print(11 in a)'''


#tuple can be nested inside a set
'''a={1,2,3,(1,2,3),11}
print(a)'''


#convert list in to a set
'''a=[1,2,3,4,5,6]
b=set(a)
print(type(b))
print(b)'''


#intersection ,union, differnce,symmetric difference
a={1,2,3,4}
b={12,1,3,11}
print(a.union(b))
print(a.intersection(b))
print(a.difference(b))
print(a.symmetric_difference(b))