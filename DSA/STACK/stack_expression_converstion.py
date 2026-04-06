def infix_to_postfix(exp):
    stack = []
    output = []
    priority = {'**':3,"^":3,"*":2,"/":2,"+":1,"-":1}

    for char in exp:
        # checking for the operand
        if char.isalnum():
            output.append(char)
        elif char == "(":
            stack.append(char)
        elif char == ")":
            while stack and stack[-1] != '(':
                output.append(stack.pop())
            stack.pop()
        else:
            while stack and stack[-1] != '(' and priority.get(char,0) <= priority.get(stack[-1],0):
                output.append(stack.pop())
            stack.append(char)
    
    while stack:
        output.append(stack.pop())
    return " ".join(output)
ex = "(a+b)*c-d"
print(infix_to_postfix(ex))


# 2 + 3 * 6 + 4 - 8 => 16
# 2 + 3 6 * + 4 - 8 => 236*+4+8-

#Postfix epression Evaluation with stack

def post_exp_eval(exp):
    stack = []
    for char in exp:
        if char.isdigit():
            stack.append(int(char))
        else:
            top_el = stack.pop() 
            nex_el = stack.pop()

            # if operator => nex_el operator top_el
            if char == '+':
                stack.append(nex_el + top_el)
            elif char == "-":
                stack.append(nex_el - top_el)
            elif char == "*":
                stack.append(nex_el * top_el)
            elif char == "/":
                stack.append(nex_el / top_el)
    return stack.pop()

postfix_exp = "236*+4+8-"
print(post_exp_eval(postfix_exp))