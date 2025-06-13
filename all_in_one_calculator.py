num1 = float(input("Enter the first number: "))
num2 = float(input("Enter the second number: "))
print("Choose operation:")
print("1. addition:")
print("2. subtraction:")
print("3. multiplication:")
print("4. division:")
print("5. power:")
print("6. remainder:")

choice = input("Enter your choice (1/2/3/4/5/6): ")

if choice == "1":
    print(num1 + num2)

elif choice == "2":
    print(num1 - num2)

elif choice == "3":
    print(num1 * num2)

elif choice == "4":
    if num2 == 0:
        print("Cannot divide by Zero")
    else:
        print(num1 / num2)

elif choice == "5":
    print(num1 ** num2)

elif choice == "6":
    if num2 == 0:
        print("Divided by zero is undefined.")
    else:
        print(num1 % num2)

else:
    print("Invalid choice:")

print("Thanks for using calculator.")

