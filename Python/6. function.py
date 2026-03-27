'''
function:
    reusability

built-in
user-defined function


argument:
    1. required/positional
    2. keyword
    3. default
    4. variable length argument
        *args: comma seperated, list, tuple. return -> tuple

        **kwargs: key = value. return -> dictionary
'''

def summ(a,b=63):
    c = a + b
    return c

print(summ(5,100))
# [1,6,3,7,2,5,9].sort(reverse = True)

def one(*args,**kwargs):
    print(args)
    print(kwargs)

one(1)
one(1,5,6,9,name="john")
one(20,1,5,9,8,6,3,2,1,45,5,name="john",college ="ABC",age = 85, marks = [2,3,5,6,7])

def summm(a,*args):
    res = a
    for i in args:
        res += i
    return res

print(summm(5))
print(summm(5,5))
print(summm(5,5,5))
print(summm(5,5,5,5,5))
print(summm(5,5,5,5,5,5,5))
print(summm(5,5,5,5,5,5,5,5,5))

'''
# Annonymous function
    single line function
    without name
    multiple argument but single execution

    python uses lambda keyword for annonymous function.
'''
# WAP to return square of a number.
def sq():
    nu = int(input("enter a number: "))
    res = nu ** 2
    print(res)
sq()

res = lambda n:n**2
print(res(52))

#WAP to multiply two given number
mu = lambda n,m:n*m
print(mu(8,6))

'''
file handling
modules/packages
exception handling
OOPs

'''







