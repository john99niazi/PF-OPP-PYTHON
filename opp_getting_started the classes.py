#simple  basic class
'''class student:
    name="junaid"

s1=student()
print(s1.name)
'''




#constructor
'''class car:
    def __init__(self):
        
        print("the car is blue")
        print("the model is 2005")
    
s1=car()'''





#area of rectangle:::::

'''class rec:
    def __init__(self,length,breath):
        print("area of rectangle is ", length*breath)


l=int(input("enter the length"))
b=int(input("enter the breath"))

s1=rec(l,b)
'''







#area of rectangle using loop
'''
class Rec:
    def __init__(self, length, breadth):
        # Calculating and printing the area of the rectangle
        print(f"Area of rectangle is {length * breadth}")

# Loop to take input and create rectangle objects three times
for i in range(0, 3):
    l = int(input(f"Enter the length of rectangle {i + 1}: "))
    b = int(input(f"Enter the breadth of rectangle {i + 1}: "))
    rectangle = Rec(l, b)

'''








'''
class student:
    def __init__(self,name,marks):
        self.name=name
        self.marks=marks
        print("adding new student in database...")
        
    def welcome(self):
        print("welsome student",self.name)
    
    def get_marks(self):
        return self.marks

s1=student("karan",23)
print(s1.name)
s2=student("arjun",44)
print(s2.name)
s2.welcome()
print(s1.get_marks())
'''







#class is the collection of two things attributes and methods(basically funcations)

'''
class student():
    def __init__(self,name,mark1,mark2,mark3):
        print("total marks are 30 each subject:::::")
        print("THE NAME OF STUDENT IS ", name)
        print(f"the   marks  in english subject  {mark1} ")
        print(f"the  marks  in math subject  {mark2} ")
        print(f"the  marks  in sci subject  {mark3} ")
        
        print(f"the avergae of three  subject marks is {mark1+mark2+mark3/3}")
        
for name in range(0,3):
    name=str(input(f"enter the name of student {name+1}:::"))
    mark1=int(input("enter the marks of english:::"))
    mark2=int(input("enter the marks of math:::"))
    mark3=int(input("enter the marks of science:::"))
    student(name, mark1, mark2, mark3)

'''


#second method
'''
class student:
    def __init__(self,name,marks):
        self.name=name
        self.marks=marks
    
    def get_avg(self):
        sum=0
        for val in self.marks:
            sum+=val
        print(f" hi {self.name} your average score is:::" , sum/3)
        

s1=student("tony staerk",[99,66,55])
s1.get_avg()

'''


'''In Python, a
 static method is a method that
 belongs to a class but doesn't access or modify the class's state.
 It is defined using the @staticmethod decorator. 
 Static methods do not require an instance of the class to be called'''
'''class MathOperations:
    @staticmethod
    def add_numbers(x, y):
        return x + y

# Calling the static method without creating an instance
result = MathOperations.add_numbers(5, 3)
print(result)  # Output: 8'''




#abstraction,encapsulation ,,inhertence, polyporphism



#abstraction 
'''Abstraction in Python Object-Oriented 
Programming (OOP) is the concept of hiding complex
 implementation details and showing only the necessary 
 features of an object. It helps in reducing complexity 
 and allows the user to focus on the essentials.
'''

from abc import ABC

class Animal(ABC):
    
    def sound(self):
        pass

class Dog(Animal):
    def sound(self):
        return "Bark"

class Cat(Animal):
    def sound(self):
        return "Meow"

# Creating instances
dog = Dog()
print(dog.sound())  # Output: Bark

cat = Cat()
print(cat.sound())  # Output: Meow


class Car:
    def __init__(self):
        self.acc = False
        self.brk = False
        self.clutch = False

    def start(self):
        self.clutch = True
        self.acc = True
        print("Car is started")

car1 = Car()
car1.start()





#encapsulation::::
'''Encapsulation in Python Object-Oriented Programming 
(OOP) is a concept where the internal state of an object is hidden from the outside world and can only be accessed or modified through methods defined by the class. This is achieved using access modifiers:

Private attributes (prefixed with __) are not 
accessible directly outside the class.
Protected attributes (prefixed with _) are intended 
to be accessed only within the class and its subclasses.
  
'''

'''
class Car:
    def __init__(self, make, model):
        self.__make = make  # private attribute
        self._model = model  # protected attribute

    def get_make(self):
        return self.__make  # access private attribute through a method

car = Car("Toyota", "Corolla")
print(car.get_make())  # Accessing the private attribute using a method



'''
    
    












