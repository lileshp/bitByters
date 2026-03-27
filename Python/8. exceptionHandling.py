'''
Exception:
    Error: semantic, syntax

    try: (required)
        write code which you want to execute
    except: (required)
        handle exception
    else:
    finally:
    
'''
def readFile():
    with open('example.txt','r') as file:
        data = file.readline()
    c = 10/10
    a = int('a10')
    return data, a

try:
    da,na = readFile()
    print(da)
    print(na)
except NameError as er:
    print(er)
except ValueError as er:
    print(er)
except ZeroDivisionError as er:
    print(er)
except:
    print("ANYTHING")
else:
    print("NO ERROR")
finally:
    print("ALWAYS with or without exception")

print("HELLO")