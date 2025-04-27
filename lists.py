#create list
a=["red","blue","green"]
print(a)

#we need single elemnt from list use indexing
b=["1","2","3"]
print(b[0])
print(b[2])
#find length using len funcation
'''c=["1","2","3","4","5"]
print(len(c))'''

#USING LOOP WITH Range()with list
d=["1","2","3","4","5"]
for i in range(len(d)):
   print(d[i])

#using """"for each loop""""" with list  for color in colors:
e=["1","2","3","4","6","7","9","10"]
for num in e:
    print(num)

#updating elemnt in list
f=["1","2","3"]
f[2]=6 #update
print(f)


#appending the elemnt to the end of list using append()
i=["1","2","3","4"]

i.append("0")
print(i)

#inserting the elemnt at a particular index
'''i=[1,2,3,4]
i.insert(1,5)
print(i)'''
#for emoving elemnet at particualr place
'''i=[1,2,3,4,5,7]
i.remove()
print(i)'''

#pop is uised to removed last elemnt in list
'''i=[1,2,3,4,5,6]
i.pop(2)
print(i)'''

#clear is used removed all elments
'''a=[1,2,3]
a.clear()
print(a)'''

#reversing the lisst
'''i=[1,3,4,5]
i.reverse()
print(i)'''

#sorting in list we ALSO SORT STRING
'''i=[1,3,4,11,0,5,2]
i.sort()
print(i)'''

#USIG INDEX WITH LIST _COLORS INDEX(ELMENTS) GET US THE INDEX OF THE ELEMT OF LIST
'''a=[1,2,3,4]
print(a)

print(a.index(3))#print index number'''

#using nested list list within list
'''a=[1,2,3,4,[7,8,9,0],11]
print(a[4][3])
'''

#we have differnet elemnt linke string boll intger
'''a=["red","greem",14.5,"petrol",True,1]
print(a)'''


#forward and backward index
a=[1,2,3,99,7]
print(a[2])#forward index
print(a[-1])#backward index  -1+5=4index

#slincing list
a=[1,2,3,4,11,22,33,44,55,66,77,88,99]
print(a[1:6])


#how elemnts repeated in the list
'''i=[1,2,3,4,4,1,2,2,2,2,3]
print(i.count(2))'''

#find maximum and minimum in list
'''i=[1,2,3,4]
print(max(i))
print(min(i))'''


'''#find sum of elemt in list
i=[1,2,3,4]
print(sum(i))'''
#whih type
'''i=[1,1.5,True]
print(type([1]))
print(type(i))'''

#delete list
'''a=[1,2]
del a
print(a)'''


#using in and not in opertor with list ////give true and fasle
'''
a=[1,2,3,4]
print(5 in a)
print(1 in a)

'''

#concatening two list using opeartor
'''a=[1,2,3,4]
b=["red ","green"]
print(a+b)
'''

# extended list
o=[1,2,3,4]
i=["blue","rend"]
o.extend(i)
print(o)
print(i)



#question one Create a list of the first 5 prime numbers and print the third element.

'''list=[2,3,5,7,11]
print(list[3])'''

#Create a list of the first 10 natural numbers and print the last 5 elements.
'''l=[1,2,3,4,5,6,7,8,9,10]
print(l[5:10])'''


#Create a list of your favorite fruits. Add a new fruit to the list and remove the first fruit from the list.
'''f=["apple","mango","orange","stobbery"]
f.append("bananan")
f.remove("apple")
print(f)'''

#Create two lists: one containing the names of your family members and 
# another containing the names of your friends. Concatenate
#  these lists into a single list and print it.
'''a=["family"]
b=["friend"]
print(a+b)'''

#List Comprehensions:

#Create a list of squares of the first 10 natural numbers using a list comprehension.
numbers=[1,2,3,4,5,6,7,8,9,10]
new_number=[num*num for num in numbers]
print(new_number)

#Filtering Lists:

#Create a list of numbers from 1 to 20. Use a list comprehension
#to create a new list containing only the even numbers.
'''nums=[1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20]
new_list=[num*2 for num in nums]
print(new_list)'''

# create a list of lists
# where each sublist contains the name and age of your family members. 
# Print the age of the second family member
family = [
    ["Alice", 34],
    ["Bob", 42],
    ["Charlie", 15]
]

# Print the age of the second family member
print(family[1][1])



#Flattening a List of Lists:

#Given a list of lists [[1, 2], [3, 4], [5, 6]], flatten it into a single list [1, 2, 3, 4, 5, 6].
'''nested_list = [[1, 2], [3, 4], [5, 6]]

# Flatten the list of lists into a single list
flattened_list = [item for sublist in nested_list for item in sublist]

print(flattened_list)'''

#Write a function that takes a list of numbers and returns the second largest element.

def second_largest(numbers):
    if len(numbers) < 2:
        return None  # Not enough elements to determine the second largest
    
    # Remove duplicates
    unique_numbers = list(set(numbers))
    
    if len(unique_numbers) < 2:
        return None  # Not enough unique elements to determine the second largest
    
    # Sort the list in descending order
    unique_numbers.sort(reverse=True)
    
    # The second largest element
    return unique_numbers[1]

# Example usage:
numbers = [3, 1, 4, 1, 5, 9, 2, 6, 5, 3, 5]
print(second_largest(numbers))  # Output: 6