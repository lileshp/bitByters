'''
conditional statements:
    if
    if else
    if - elif - else (Ladder if)
    nested if

'''
age = 45
if age >= 18:
    print("You are eligible for voting!!!")


# EVEN ODD
num = 6
if num%2 == 0:
    print("EVEN")
else:
    print("ODD")

# student grades (Ladder if)
per = -100 #invalid
if per >= 85 and per <= 100:
    print("Your Grade is A+")
elif per >= 75 and per < 85:
    print("Your Grade is A")
elif per >= 60 and per < 75:
    print("Your Grade is B")
elif per >= 45 and per < 60:
    print("Your Grade is C")
elif per >= 0 and per < 45:
    print("You are Fail")
else:
    print("Invalid Percentage")


#Nested IF
'''
    semester: 7
    branch: CSE
    bakclog: yes
    CGPA: > 8

    execution: Eligible for campus
'''
sem = 7
branch = "CSE"
backlog = "Y"
cgpa = 8.2

# if sem == 7 or sem == 8 and branch == "CSE" and backlog == "N" and cgpa >= 8:


if sem == 7 or sem == 8:
    if branch == "CSE":
        if backlog == "N":
            if cgpa >= 8:
                print("You are eligible for voting")
            else:
                print("Your CGPA is low")
        else:
            print("You have backlogs")
    else:
        print("Only CSE students")
else:
    print("Only 7th and 8th semester students")

'''
LOGIN
    username
        password
    Login

'''