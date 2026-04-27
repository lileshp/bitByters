'''
RECURSION

What:
    is a programming technique where a function calls itself to solve a problem.
    The function continues to call itself with a smaller subset of the original problem until it reaches a base case that use to stops the recursion.

Why:
    1. Eliminates loop constructs:
    2. Simplifies complex problems
    3. Mathematical computation
    4. Tree & Graph Traversal

Application:
    Mathematical computation: Factorial, Fibonacci, GCD, Tower of Hanoi
    Tree and Graph: DFS, BST operations
    Divide & Conquer: Binary Search, Merge Sort, Quick Sort
    Backtracking Algorithms: N-Queen Problem, Maze solving, Sudoku solver
    Dynamic Programming: Memoization-based solution

When to use recursion:
    when a problem can be broken into smaller subproblems of the same type.
    1. Divide & Conquer Algorithm
    2. Tree & Graph Traversal
    3. Backtracking Algorithms
    4. DP
    5. Mathematical computation

Limitations of the recursion:
    1. Difficult to debug and understanding -> use proper print function
    2. High Memory usage (Stack overflow) -> use iterative approaches
    3. Slower Execution: 
    4. Not always efficient:

Types of Recursion:
    1. Direct/Linear/Simple: The function calls itself directly.
    2. Indirect: Function A calls Function B and Function B calls Function A.
    3. Tree Recursion: when a function makes multiple recursive calls.
    4. Head Recursion: The recursive call is the first operation in the function
    5. Tail Recursion: The recursive call is the last operation in the function
    6. Nested Recursion: A recursive function calls itself as an argument to another recursive call.
'''
# Direct Recursion
def factorial(n):
    if n == 0:
        return 1
    return n * factorial(n-1)

# print(factorial(5))

# Indirect Recursion
def is_even(n):
    if n == 0:
        return True
    return is_odd(n - 1)

def is_odd(n):
    if n == 0:
        return False
    return is_even(n - 1)

# print(is_even(3))

#Head Recursion
def head_recursion(n):
    if n == 0:
        return
    head_recursion(n - 1)
    print(n, end = " ")

# head_recursion(5)

#Tail recursion
def tail_factorial(n, a = 1):
    if n == 0:
        return a
    return tail_factorial(n - 1,n * a)

# print(tail_factorial(5))

def nested_recursion(n):
    if n > 100:
        return n - 10
    return nested_recursion(nested_recursion(n + 11))

# print(nested_recursion(80))

#Tree Recursion
def fabonacci(n):
    if n <= 1:
        return n
    return fabonacci(n-1) + fabonacci(n-2) # two recursive calls
# print(fabonacci(6))


# Solve With Recursion

# Reverse a string
def reverse_string(s):
    if len(s) == 0:
        return s
    return s[-1] + reverse_string(s[:-1])  # Recursive call

print(reverse_string("hello"))  # Output: "olleh"

# Addition of digits in given number
def sum_of_digits(n):
    if n == 0:  # Base case
        return 0
    return (n % 10) + sum_of_digits(n // 10)  # Recursive call

print(sum_of_digits(123450))

# check that given string is palindrome
def is_palindrome(s):
    if len(s) <= 1:
        return True
    if s[0] != s[-1]:
        return False
    return is_palindrome(s[1:-1])  # Recursive call

print(is_palindrome("madam"))

# implement binary search with recursion
def binary_search(arr, low, high, x):
    if low > high:
        return -1
    mid = (low + high) // 2
    if arr[mid] == x:
        return mid
    elif arr[mid] > x:
        return binary_search(arr, low, mid - 1, x)
    else:
        return binary_search(arr, mid + 1, high, x)

arr = [1, 3, 5, 7, 9, 11]
print(binary_search(arr, 0, len(arr) - 1, 5))