user_password="jayadev@123"
while True:
    user_input=input("Enter your password: ")
    if user_input==user_password:
        print("Password is correct!")
        break
    else:
        print("Incorrect password. Please try again.")