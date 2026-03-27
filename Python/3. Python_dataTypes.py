'''
    Numbers:
        int()
        float()

        immutable object
        not iterable
        not indexable
        not subscriptable

        all arithmatic operator using with numbers
        we can use math module

        dir() -> to check all functionality of module.
'''

'''
a = 10
print(type(a))
print(dir(int))
print(int.__name__)
'''

'''
String:

    str()
    a-zA-Z0-9~!@#$%^&*()_+{:"} enclosed in quotes (single, double)

    a = '10'
    b = "10"
    c = """10"""
    d = 

    immutable object
    iterable object
    subscriptable
    indexable

    Slicing
        [start:stop:steps]
        start: 0 (Default)
        stop: required
        steps: 1 (default)

    concatenation: +
    repeat: *
'''

bio = """
fdkjg
dflskgjdfs
lkdfjsg


fdlksgjlkdf
ldfjslkgj
mcnv;d;f

"""

i_it = iter('bhopal')
print(next(i_it))

print("Hello")

for i in range(10000):
    print(i)
print(next(i_it))
print(next(i_it))
print(next(i_it))
print(next(i_it))
print(next(i_it))
print(next(i_it))

'''
LIST:
    list()
    []

    mutable object
    iterable
    subscriptable
    indexable

    add: +
    list element repeat: *

    slicing operator:
        [:]
'''

# shift all zeros on right side from given array.
# ar = [1,0,3,4,0,0,6,7,0,8,0,9,2]
# out = [1,3,4,6,7,8,9,2,0,0,0,0,0]
arr = [1,0,3,4,0,0,6,7,0,8,0,9,2]
ar = [0] * len(arr)

'''
Dictionary:

mapped data

dict()
{}

unordered collection
subscriptable
iterable
mutable

keys: all immutable objects
values: all arbitary data

d = {1:1,'two':2,(1,2):'lilesh'}
'''

d = {1:100,2:200}
d[2] = 300
print(d)
d[30] = 1000
print(d)

print(dir(dict))
print(d.get(1,"Please check your field"))

print(d.values())
print(d.items())

d = {1:100,2:200}
# print(d.pop(1))
print(d.popitem())

d = {1:100,2:200,3:300,4:400}
for key,val in d.items():
    if val == 300:
        print(key)

'''
set:


    unordered collection unique
    set()
    {}

    mutable
    iterable
    not indexable

frozenset:

    immutable
    not indexable
    iterable
'''

l = [i for i in range(1,20)]
s =set(l)
s = {1,1,2,3,4,5,7,8,96,4,32,12,4,5,6,2,3,1,5}
print(s)