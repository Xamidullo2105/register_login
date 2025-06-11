from utils import send_email
from file_manager import append, read, writerows
import random


def register():
    full_name = input("Enter your full name: ")
    email = input("Enter your email: ")
    password1 = input("Enter your password: ")
    password2 = input("Enter your password again: ")
    
    
    while password1 != password2:
        password1 = input("Enter your password: ")
        password2 = input("Enter your password again: ")

    otp = random.randint(1000, 9999)

    send_email(receiver_email=email, body=str(otp))
    append(filename="users",data=[full_name, email,password1])
    append(filename="codes", data=[email, otp])
    return check_otp(otp, email)


def login():
    email = input("Enter your email: ")
    password = input("Enter your password: ")
    
    users = read("users")
    for row in users:
        if len(row) < 3:
            continue
        
        full_name = row[0].strip()
        user_email = row[1].strip()
        user_password = row[2].strip()
        
        if email == user_email and password == user_password:
            print(f"Login seccessful ✅. Welcome {full_name}")
            return True

    print("Login failed. Invalid email or password ❌")
    return False


def logout(filename="users"):
    users = read(filename)
    updated = []
    for row in users:
        if len(row) >= 5:
            row[4] = "False"
        updated.append(row)
        
    writerows(filename, updated)
    print("All users have been logged out ✅")


def check_otp(expected_code, email, filename="users"):
    code = input("Enter the code: ")
    success = code == str(expected_code)
    
    users = read(filename="users")
    updated = []
    
    for row in users:
        if len(row) >= 3 and row[1] == email:
            if success:
                updated.append(row + ["True"])
            else:
                updated.append(row + ["False"])
        else:
            updated.append(row)
            
    writerows(filename, updated)
    return success