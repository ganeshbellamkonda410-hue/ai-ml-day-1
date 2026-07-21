correct_username = "admin"
correct_password = "python123"
attempts = 3
while attempts > 0:
    username = input("Enter Username: ")
    password = input("Enter Password: ")
    if username == correct_username and password == correct_password:
        print(" Welcome! Login Successful.")
        break
    else:
        attempts -= 1
        if attempts > 0:
            print(" Invalid Username or Password.")
            print("Attempts left:", attempts)
        else:
            print(" Account Locked!")
