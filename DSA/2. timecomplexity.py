#WAP to return sum and product of the given array
ar = [3,4,6,2,3,8,9,4,5]

def f(ar):
    sum = 0
    product = 1

    for i in ar:
        sum += i

    for j in ar:
        product *= j
    return sum, product


#WAP to reverse array

def powerOf2(n):
    if n < 1:
        return 0
    elif n == 1:
        print(1)
        return 1
    else:
        prev = powerOf2(int(n/2))
        curr = prev * 2
        print(curr)
        return curr
    
print(powerOf2(50))