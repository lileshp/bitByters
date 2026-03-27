print(10 + 10) #__add__
print('a' + 'b') #__add__

def add(a,b):
    return a + b

print(add(5,20))
print(add('Hello ',"Brother"))

'''
Polymorphism:
    Same method name, but different implementation basis on the input size and type.

    Compile Time: Method overloading
    Run Time: Method overriding

syntax checking
error: compile
code conversion: HLL to ML/BL
memory allocation

constructor overloading
'''

class CSE:
    def __init__(self,*args):
        print("EXAM A")
    def show(self):
        pass

class AIML(CSE):
    def __init__(self,a,b):
        print("CLASS AIML")
    def show(self):
        pass
obj = CSE(6,6)
obj.exam()

class Auction:
    def __init__(self,product,price = 40000):
        self.product = product
        self.price = price

        if price <= 40000:
            print("Sold of base price")
        else:
            print("Sold on high price")

john = Auction('Laptop')
sam = Auction('Car',100000)

class Notification:
    def send(self):
        pass

class Email(Notification):
    def send(self):
        pass

class Message(Notification):
    def send(self):
        pass
    
