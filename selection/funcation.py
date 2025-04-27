
# Basic Functions
'''def greet():
    print("hello worls")
greet()'''


##Functions with Parameters
'''def greet(name):
    print(f"heloo {name}")
greet("junaid")'''

# Functions with Return Values
'''def add(a,b):
    return a+b
sum=add(4,5)
print(sum)'''

#Default Parameters
#Functions can have default parameter values, which are used if no argument is provided.
'''def greet(name="khan"):
    print(f"junaid {name}")
greet()
greet("niazi")'''

#User-defined Functions
#These are functions that you define yourself to perform specific tasks. They can have parameters and return values.

#Basic User-defined Function

'''def greet(name):
    return f"Hello, {name}!"

print(greet("Alice"))  # Output: Hello, Alice!'''

#Function with Default Parameters

def greet(message,name="junaid"):
    return f" {name} {message}"
#print(greet("hey"))
print(greet("bye","niazi3 "))
