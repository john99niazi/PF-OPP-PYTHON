#class object method ,inheritance ,polymorphism ,encapsilation ,abstraction
# in pascalCase we write the name of class
#for object name and variable we used snake_case
'''class student:
    pass

s1=student()
s1.name="jun"
s1.id=12
print(s1.name,s1.id)'''

'''class student:
    def __init__(self,name,id,mark):
        self.name=name
        self.id=id
        self.mark=mark
    
    def display_name(self):
        print(f"my name is{self.name}")
        print(f"my id is{self.id}")
        print(f"my marks are{self.mark}")

s1=student(name="junaid",id="2019",mark="300")
s1.display_name()
'''
#without constructorrr
'''
class students:
    def enter_name(self):
        self.name=str(input("enter the name of student:::"))
        self.id=int(input("enter the id of student:::"))
    
    def display(self):
        print("the name of student is" ,self.name)
        print("the name of student is" ,self.id)

s1=students()
s1.enter_name()
s1.display()'''

#constructor
class book:
    def __init__(self,title,author,year):
        self.title=title
        self.author=author
        self.year=year
    def display(self):
        print(f"THE NAME OF BOOK IS:::{self.title}")
        print(f"THE NAME OF AUTHOR IS:::{self.author}")
        print(f"THE YEAR THE BOOK IS  PUBLIS:::{self.year}")

b1=book(title="HAARY POTTER", author="khan" ,year= "2011")
b2=book(title="marry chirisss" , author=" ali muhammad" ,year= "2015")
b1.display()
b2.display()
        

      