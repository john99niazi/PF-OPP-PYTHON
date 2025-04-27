#PRIVATE METHOD


class Person:
    __name = "anonymous"  # Private attribute

    def __hello(self):  # Private method
        print("HELLO PERSON")

    def welcome(self):
        self.__hello()  # Accessing the private method within the class

p1 = Person()
p1.welcome()  # This will call the private method indirectly



#inhertance

class Animal:
    def speak(self):
        print("Animal sound")

class Dog(Animal):  # Dog inherits from Animal
    def speak(self):
        print("Bark")

# Create instances
animal = Animal()
dog = Dog()

animal.speak()  # Output: Animal sound
dog.speak()     # Output: Bark



#multiple inheritanec
#multiple inheritance in Python, where a child 
#class inherits from more than one parent class:
# Parent class 1
class Engine:
    def start_engine(self):
        print("Engine started.")

# Parent class 2
class Radio:
    def play_radio(self):
        print("Radio is playing.")

# Child class inheriting from both Engine and Radio
class Car(Engine, Radio):
    def drive(self):
        print("Car is driving.")

# Creating an object of the Car class
my_car = Car()
my_car.start_engine()  # Method from Engine class
my_car.play_radio()    # Method from Radio class
my_car.drive()         # Method from Car class



#multiplevel inheritance
# Base class
class Animal:
    def sound(self):
        print("Some generic animal sound")

# Derived class inheriting from Animal
class Dog(Animal):
    def bark(self):
        print("Dog barks")

# Another derived class inheriting from Dog
class Puppy(Dog):
    def play(self):
        print("Puppy plays")

# Creating an object of Puppy class
my_puppy = Puppy()
my_puppy.sound()  # Method from Animal class
my_puppy.bark()   # Method from Dog class
my_puppy.play()   # Method from Puppy class



#super method class
#The super() method in Python's object-oriented programming (OOP) 
#is used to call methods from a parent (or base) class within a child
# (or derived) class. It provides a way to access methods and properties
# of the parent class, allowing us to extend or modify their behavior.

class Animal:
    def __init__(self, name):
        self.name = name

class Dog(Animal):
    def __init__(self, name, breed):
        super().__init__(name)  # Call the parent class's __init__ method
        self.breed = breed

dog = Dog("Buddy", "Golden Retriever")
print(dog.name)  # Output: Buddy
print(dog.breed)  # Output: Golden Retriever



#polyporphism
#Polymorphism allows objects of different classes
 #to be treated as objects of a common superclass.
 #It enables the same method name to be used for 
 #different types (or classes). The specific method
 #that gets executed is determined by the object calling it.
class Dog:
    def sound(self):
        return "Woof!"

class Cat:
    def sound(self):
        return "Meow!"

def animal_sound(animal):
    print(animal.sound())

dog = Dog()
cat = Cat()

animal_sound(dog)  # Output: Woof!
animal_sound(cat)  # Output: Meow!


#operator overloading
#Operator overloading allows you to define the behavior
#of operators (+, -, *, etc.) for user-defined classes.
#You can do this by defining special methods in your class.
class Vector:
    def __init__(self, x, y):
        self.x = x
        self.y = y
    
    def __add__(self, other):
        return Vector(self.x + other.x, self.y + other.y)

    def __repr__(self):
        return f"Vector({self.x}, {self.y})"

v1 = Vector(2, 3)
v2 = Vector(5, 7)
result = v1 + v2  # Uses the __add__ method
print(result)      # Output: Vector(7, 10)





