'''
Database connectivity:


'''


import mysql.connector as my
import hashlib

# db_sql = "create database bitbyte"
# tb_sql = "create table users (id int auto_increment primary key, username varchar(50), password varchar(50),email varchar(50))"
def connectdb():
    conn = my.connect(host="localhost",user="root",password="",database="bitbyte")
    return conn

def enc_pwd(password):
    return hashlib.sha256(password.encode()).hexdigest()

def register():
    con = connectdb()
    cur = con.cursor()

    uname = input("Enter your username: ")
    email_id = input("Enter your Email: ")
    pwd = input("Enter your password: ")

    cur.execute("select * from users where username = %s", (uname,))
    if cur.fetchone():
        print("User Already exists!!")
        return
    
    sql = "insert into users (email,username,password) values(%s,%s,%s)"

    val = (email_id,uname,pwd)

    cur.execute(sql,val)
    con.commit()

    cur.close()
    con.close()    

# register()

def login():
    con = connectdb()
    cur = con.cursor

    attempt = 3
    while attempt > 0:
        username = input("Enter your username: ")
        password = enc_pwd(input("Enter your password: "))

        cur.execute("select * from users where username = %s and password = %s",(username,password))

        if cur.fetchone(): #fetchall()
            print("Login Successfult!!!")
            return username
        else:
            attempt -= 1
            print(f"Invalid Credentials! Attempt Left: {attempt}")
    
    print("Your Account is temporarly locked for 24 hours")
    return None

def changePassword():
    pass

def forget_password():
    pass

def changeUsername():
    pass

def logout():
    pass


def main():
    current_user = None
    while True:
        print("""
            1. Registration
            2. Login
            3. Forgot password
            4. Exit
        """)
        choice = input("Your option: ")

        if choice == '1':
            register()
        elif choice == '2':
            current_user = login()
            if current_user:
                while True:
                    print("""
                        1. Show Profile
                        2. Update Profile
                        3. Logout
                        """)
                    choice = input("enter choice: ")
                    if choice == '1':
                        pass
                    elif choice =='2':
                        pass
                    elif choice == '3':
                        break
                    else:
                        print("Invalid input")
        elif choice == '3':
            forget_password()
        elif choice == '4':
            break