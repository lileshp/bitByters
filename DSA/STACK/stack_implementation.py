#Dynamic Stack
class Stack:
    def __init__(self):
        self.stack = []
    def push(self,ele):
        self.stack.append(ele)
    def pop(self):
        if self.is_empty():
            return "Stack is Underflow!"
        return self.stack.pop()
    def is_empty(self):
        return len(self.stack) == 0
    def peek(self):
        if self.is_empty():
            return "Stack is Empty!"
        return self.stack[-1]
    def display(self):
        return self.stack
    
'''
st = Stack() #st.stack = []
# el = st.pop()
# print(el)
st.push(89)
st.push(12)
st.push(36)
st.pop()
st.push(56)
st.pop()
st.pop()
st.push(200)
print(st.display())
'''

#STATIC STACK
class StaticStack:
    def __init__(self, capacity):
        self.capacity = capacity
        self.stack = [None] * capacity
        self.top = 0 # -1
    
    def push(self, ele):
        if self.top == self.capacity: #self.top == self.capacity - 1
            print("Stack is Overflow!! We cannot perform PUSH Ops!!")
            return
        self.top += 1
        self.stack[self.top] = ele
        print(f"ADDED {ele} in Stack")
    
    def pop(self):
        if self.top == 0:
            print("Stack is UNDERFLOW Condition We cannot popout any element")
            return
        element = self.stack[self.top]
        self.stack[self.top] = None # no need in python
        self.top -= 1
        return element

    def peek(self):
        if self.top == 0:
            return "Stack is Empty!"
        return self.stack[self.top]
    
    def is_full(self):
        return self.top == self.capacity
    
    def display(self):
        return self.stack

stack = StaticStack(6)
print(type(stack))
print(stack.display())
stack.push("Hello")
stack.push("Namaste")
stack.pop()
stack.push("Hi")
print(stack.display())

# VALID SYMBOLS
def is_valid(sym):
    stack = []
    mapping = {")":"(","}":"{","]":"["}
    for char in sym: #(
        if char in mapping:
            top_ele = stack.pop() if stack else "#"
            if mapping[char] != top_ele: #
                return False
        else:
            stack.append(char)
    return len(stack) == 0


symbols = "([]){{}[}]"
res = is_valid(symbols)
if res:
    print("VAlid Symbols")
else:
    print("INvalid pairs of symbols")


# next greater element

def next_greater_element(arr):
    n = len(arr)
    res = [-1] * n
    stack = []
    for i in range(n-1, -1, -1):
        while stack and stack[-1] <= arr[i]:
            stack.pop()
        if stack:
            res[i] = stack[-1]
        stack.append(arr[i])
    return res
arr = [1,2,3,4]
print(next_greater_element(arr))

# Circular array: [40,3,10,6] => [-1,10,-1,40]



#WAP to check Valid brackets/symbols
inp = "([])[]()[][]"



"""
PROJECTS
    Management system
    E-commerce
    Quick-commerce
    Social MEdia
    booking system
    Streaming
    Games
    


"""

