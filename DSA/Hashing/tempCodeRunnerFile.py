def duplicate(ar):
    s = set()
    for i in ar:
        if i not in s:
            s.add(i)
        else:
            return True

ar = [4,3,2,1,5]
res = duplicate
print(res)
if res:
    print("Duplicate element in the array")
else:
    print("Unique element in the array")