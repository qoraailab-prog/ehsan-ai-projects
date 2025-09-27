name = input("Enter your name: ")
age = input("Enter your age: ")
student = input("Are you a student? (yes/no): ")
city = input("Enter your city: ")
height = input("Enter your height in cm: ")
likes_ai = input("Do you like Artificial Intelligence? (yes/no): ")

print(f"Name: {name}, Age: {age}, Student: {student}, City: {city}, Height: {height}")

if likes_ai.lower() == "yes":
    print("I love Artificial Intelligence!")
else:
    print("I am not interested in Artificial Intelligence.")
