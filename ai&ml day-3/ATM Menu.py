balance=100000
while True:
    print("Welcome to the ATM!")
    print("1. Check Balance")
    print("2. Withdraw Money")
    print("3. Deposit Money")
    print("4. Exit")
    
    choice = input("Enter your choice (1-4): ")
    
    if choice == '1':
        print(f"Your current balance is: ${balance}")
    elif choice == '2':
        amount = float(input("Enter the amount to withdraw: "))
        if amount > balance:
            print("Insufficient funds.")
        else:
            balance -= amount
            print(f"You have withdrawn ${amount}. Your new balance is: ${balance}")
    elif choice == '3':
        amount = float(input("Enter the amount to deposit: "))
        balance += amount
        print(f"You have deposited ${amount}. Your new balance is: ${balance}")
    elif choice == '4':
        print("Thank you for using the ATM. Goodbye!")
        break
    else:
        print("Invalid choice. Please try again.")