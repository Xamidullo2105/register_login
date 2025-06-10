from utils import send_email
from file_manager import append


def register():
    full_name = input("Enter your full name: ")
    email = input("Enter your email: ")
    password1 = input("Enter your password: ")
    password2 = input("Enter your password again: ")
    
    
    while password1 != password2:
        password1 = input("Enter your password: ")
        password2 = input("Enter your password again: ")

    send_email(receiver_email=email, body="0000")
    append(filename="users",data=[full_name, email,password1])


def login():
    pass



def logout():
    pass