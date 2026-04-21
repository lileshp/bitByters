#Longest Consecutive Sequence in given array
# ar = [100,104,200,103,105,101,5]
def longest_sequence(arr):
    s = set(arr) #unordered, not indexable
    longest = 0 #4
    for i in s:
        if (i-1) not in s: #
            curr_num = i #
            streak = 1 #
            while curr_num + 1 in s:   # 1+ 1 = 2 
                curr_num += 1 #4
                streak += 1 #4
            longest = max(longest, streak) #(0,1) 1
    return longest

ar = [100,104,200,103,102,101,5]
print(longest_sequence(ar))

#frequency count of element in given array
def freq(arr):
    occ = {} #{1:2,2:1,3:1}
    for i in arr:
        occ[i] = occ.get(i,0) + 1
    return occ

arr = [1,2,3,1,2,3,4,2,3,1]
print(freq(arr))

# subarray with sum 0
# First Non-repeating character: abcdab
def fnr(string):
    count = {}
    for char in string: count[char] = count.get(char,0) + 1
    for ind,val in enumerate(string):
        if count[val] == 1:
            return string[ind]
    return -1

st = "abcdab"
print(fnr(st))

#second non-repeating character

#WAP to find duplicates in array
def duplicate(ar):
    s = set()
    for i in ar:
        if i in s: return True
        s.add(i)
    return False
ar = [4,3,2,1,5]
res = duplicate(ar)
print(res)
if res:
    print("Duplicate element in the array")
else:
    print("Unique element in the array")

#remove duplicate from an array  Space O(1) (2 pointer)