# Dynamic Multiplication Table

while True:
    try:
        n = int(input("Enter the maximum number for the multiplication table (e.g., 10, 20, 30): "))
        if n > 0:
            break
        else:
            print("Please enter a positive number greater than 0.")
    except ValueError:
        print("Invalid input! Please enter a valid integer.")

print("    ", end="")
for i in range(1, n + 1):
    print(f"{i:4}", end="")
print("\n" + "-" * (4 * n + 5))

for i in range(1, n + 1):
    print(f"{i:2} |", end="")   
    for j in range(1, n + 1):
        print(f"{i*j:4}", end="")
    print()

