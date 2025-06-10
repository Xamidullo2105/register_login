from views import register


def main():
    print("""
        1.Register
        2.Login
        3.Logout
        """)
    
    
    choice = input("Enter your choice: ")
    if choice == "1":
        register()
    elif choice == "2":
        pass
    elif choice == "3":
        print("Good bye:)")
        return
    else:
        print("Invalid choice")


if __name__ == "__main__":
    main()