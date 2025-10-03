while True:
    # Input 'a' with validation
    while True:
        try:
            a = int(input("Enter number a: "))
            if a > 0:
                break
            else:
                print("Please enter a positive integer for a.")
        except ValueError:
            print("Invalid input! Please enter a valid integer for a.")

    # Input 'b' with validation
    while True:
        try:
            b = int(input("Enter number b: "))
            if b > 0:
                break
            else:
                print("Please enter a positive integer for b.")
        except ValueError:
            print("Invalid input! Please enter a valid integer for b.")

    # Input 'n' (repeat count) with validation
    while True:
        try:
            n = int(input("Enter how many times to repeat: "))
            if n > 0:
                break
            else:
                print("Please enter a positive integer for the repeat count.")
        except ValueError:
            print("Invalid input! Please enter a valid integer for the repeat count.")

    # Print the multiplication table
    for i in range(1, n + 1):
        print(f"{a} * ({b} + {i}) = {a * (b + i)}")

    # Ask the user if they want to continue or exit
    while True:
        again = input("Do you want to enter new numbers? (y/n): ").lower()
        if again in ['y', 'n']:
            break
        else:
            print("Invalid input! Please enter 'y' or 'n'.")

    if again == 'n':
        print("Program ended. Goodbye!")
        break
