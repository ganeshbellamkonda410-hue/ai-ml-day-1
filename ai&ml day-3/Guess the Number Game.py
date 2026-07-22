secret_num=10
while True:
    guess=int(input("Guess the number: "))
    if guess==secret_num:
        print("Congratulations! You guessed the number.")
        break
    elif guess<secret_num:
        print("lower! Try again.")    
    else:
        print("higher! Try again.")