'''
Getter -> Method to access data
Setter -> Method to modify data

used in encapsulation

control access to private variables

'''
class CSE:
    def __init__(self,marks):
        self.__marks = marks
    
    @property
    def marks(self): #Getter
        return self.__marks

    @marks.setter
    def marks(self,marks):
        if marks >= 0 and marks <= 100:
            self.__marks = marks
        else:
            print("Invalid Marks")

    def change_marks(self,value):
        self.__marks = value
obj = CSE(85) #obj.__marks = 85
print(obj.marks)

obj.marks = 90 
print(obj.marks)


'''
Generator
    is a function that values one at a time
    generator function uses yield in place of return

uses: 
'''
def counter(n):
    i = 1
    ls =[]
    while i <= n:
        ls.append(i)
        i += 1
    return ls

res = counter(5000000)
print(res)


#Generator
def counter(n):
    i = 1
    while i <= n:
        yield i
        i += 1

res = counter(50)
print(next(res))
print(next(res))
print(next(res))


tu = (i for i in range(1,30))
for i in tu:
    print(i, end=" ")


# Decorator
# is a function that modifies another function behavior

def decorator(func):
    def wrapper():
        print("First")
        func()
        print("LAST")
    return wrapper
@decorator
def greet():
    print("HELLO")

greet()


def login_required(func):
    def wrapper(user):
        if user == "admin":
            return func(user)
        else:
            print("ACCESS DENIED")
    return wrapper

@login_required
def product(user):
    print("Welcome to Product")

product("account")

def up(f):
    def inner(st):
        a = f(st)
        for _ in range(a):
            print("HEllo")
    return inner


@up
def co(st):
    res = len(st)
    return res

print(co("Hello world"))



#DECORATOR
def uper(f):
    def inner():
        return f().upper()
    return inner

def style(f):
    def inner():
        return f() + "!!!"
    return inner

def extraSpace(f):
    def inner():
        return f().strip()
    return inner

@extraSpace
@style
@uper
def greet():
    return "      Welcome in Bhopal   "

print(greet())
'''
order of decorators? Bottom -> top
    print(extraSpace(style(uper(greet()))))
Why need multiple decorators:

    
'''

class A():
    city = "Delhi" #Static Variable
    def show(self):
        print("SHow Method")
    @staticmethod
    def square(num):
        return num ** 2
print(A.square(52))
print(A.city)

# Composition (HAS-A Relationship)
# class contains another class object

# IS - A Relationship -> Inheritance
class Engine:
    def start(self):
        print("Engine Starts")
    def stop(self):
        print("Engine Stop")
class Car:
    def __init__(self):
        self.engine = Engine()
tata = Car()
tata.engine.start()


#AGGregation: Weak Relationship (objects exist independently)
class Student:
    def __init__(self,name):
        self.name = name

class CSE:
    def __init__(self,std):
        self.student = std
    def __del__(self): 
        print("Destructor")

john = Student("John")
course = CSE(john)


a = 100
print(a)
del a
print(a)

print(dir(str))

'''
Object based programming
functional programming
OOP -> object oriented programming

class:
    attribute
    methods
object
features of oop: (What, types, dependencies, programs)
    1. Inheritance
    2. Polymorphism
    3. Encapsulation
    4. Abstraction
constructor
overloading & overriding
MRO concept
super()
getter, setter, destructor
generator, decorator
static method
types of variable in the class: class/static, instance, local
SOLID Principal
composition, aggregation

'''