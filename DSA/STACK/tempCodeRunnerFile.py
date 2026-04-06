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