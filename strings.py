#strings three ways to define strings
first_name="junaid"
last_name='khan'
loc=str("niazi")

print(first_name ,last_name , loc)

#type
print(type(first_name))

#lenth of string means size
print(len(first_name),len(last_name),len(loc))

#indexing to get name
print(first_name[0])


#using for loop

for c in first_name:
    print(c)


#not in firstname
print("j" not in first_name)
print("u" not in first_name)
print("j"  in first_name)

#slicing strings
print(first_name[0:4])
print(last_name[0:4])


#modifing strings  replace charcter

print(first_name.upper())
print(last_name.lower())
print(loc.upper())

print(first_name.replace("j","n"))#replace

print(first_name.split())#split dunation

#removing leading and trailing spacces "leading space, junaid niazi ,trailing space"
b="   junaid niazi  "
print(b.strip())


#




