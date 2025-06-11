from views import register, login, logout


def main():
    
    print("""
        $*********************$    
        |    1. Register      |
        ***********************
        |    2. Login         |
        ***********************
        |    3. Logout        |
        $*********************$
        """)
    
    
    choice = input("Enter your choice: ")
    
    if choice == "1":
        if register():
            print("You can login now")
        else:
            print("Code is invalid")
            
    elif choice == "2":
        login()
    
    elif choice == "3":
        logout()
    
    else:
        print("Invalid choice")
    return main()


if __name__ == "__main__":
    main()