'''
Loop:
    repeat a code of block multiple times.
        1. you know the number of iteration - for 

        for variable in sequence:
            # code block

        sequence data: List, Tuple, set, frozenset, dictionary, string
        2. until a condition is satisfied - while

        while condition:
            Code block
            inc/dec

        range() ->
        range(start,end,steps)
            start: 0 (default)
            end: required
            steps: 1 (default)
'''

for i in range(11):
    print(i,end = " ")

for _ in range(10):
    print("HELLO", end = " ")

ls = [45,78,96,32,15,20,45,97,36]
for ind,val in enumerate(ls):
    print(f"{ind} = {val}") #placeholder

c = 1
while c <= 10:
    c += 1
    print(c)

'''
Control statments:
    break
    continue
    pass
'''

for i in range(1,20):
    if i == 11:
        break
    print(i, end=" ")
else:
    print("Loop executed successfully")

'''
else:
    execute immediate after for/while loop execution
    check that loop execute till end.

'''
print("HELLO")


'''
comprehension:
    1. List
    2. dictionary
    3. set
'''

# create a list of numbers from 120 to 430 which is divisible by 7 and multiple of 5.

ls = []
for i in range(120, 431):
    if i % 5 == 0 and i %7 == 0:
        ls.append(i)
print(ls)

lst = [i for i in range(120,431) if i %5==0 and i %7 == 0]
print(lst)

# create a dictionary of numbers and their square from 120 to 430 which is divisible by 7 and multiple of 5.

di = {}
for i in range(120, 431):
    if i % 5 == 0 and i %7 == 0:
        di[i] = i * i
print(di)

di1 = {i:i**2 for i in range(120,431) if i %5==0 and i %7 == 0}
print(di1)


tup = (i for i in range(120,431) if i %5==0 and i %7 == 0)
print(next(tup))
print(next(tup))