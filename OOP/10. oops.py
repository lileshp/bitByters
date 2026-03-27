'''
Procedural
functional

OOP - Object Oriented programming 

Real World entity

users:
    Students, Faculty, HOD, principal, Admin, SuperAdmin, Account, HR

    
Class: A blueprint for the future objects.
    Attributes (Variable): Characterstics
    Methods (Function): Behavior
Object: an instance of class

Features/pillars of oop
1. Inheritance: Sharing
2. Polymorphism: same name
3. Encapsulation: Security 
4. Abstraction: Hiding

'''
'''
class CSE:
    city = "BHOPAL"
    college = "ABC"

    def reg(self,name,branch):
        self.name = name
        self.branch = branch
        return f"Hello {self.name} welcome in {self.branch}"

john = CSE()
print(john.city)
print(john.reg("john","CSE"))
'''

#Constructor
'''
    constructor is a method
    constructor is automatically called on object creation
    constructor is used to initalize class member variables.
    In python we are using __init__() to create constructor
'''
a = 10
class CS:
    city = "BHOPAL"   # Class/Static variable
    def __init__(self,en,sec,name):
        self.enroll = en # instance variable
        self.section = sec
        self.name = name
        print(f"Welcome {self.name}")
    def regi(self,sem):
        year = 2026 # local
        self.semester = sem # instance variable
        print(f"Hello {self.name}, you enrolled for CSE branch in section {self.section}")

    def exam(self):
        pass

    def practical(self):
        pass



john = CS("CS12345","A","John")
john.regi("VI")


"""
Inheritance:
    Types:
        1. Single
        2. Multiple
        3. Multilevel
        4. Hybrid
        5. Heirarichal
"""
class A:
    def show(self):
        print("SHOW A")
class B:
    def show(self):
        print("SHOW B")
class C(B,A,object):
    pass
obj = C()
obj.city = "DELHI"
obj.show()
print(obj.city)

#MRO -> Method Resolution Order
'''
C3 Linearization

'''
print(C.__mro__)


'''
# How we can call parent class constructor in child class constructor
    super()
    via parent class Name
'''

class CSE:
    def __init__(self,a,b):
        self.enroll = a
        self.branch = b
        print("CSE Constructor")

class IT(CSE):
    def __init__(self,x,y):
        self.college = x
        self.year = y
        # CSE.__init__(self)
        super().__init__() #first inheritated parent class constructor
        print("IT Constructor")
obj = IT()