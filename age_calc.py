try:
    age = int(input("Enter your current age: "))
    years = int(input("Enter the number of years in the future: "))

    future_age = age + years
    print(f"Hello!, you will be {future_age} years old after {years} years.")
except ValueError:
    print("Please enter valid number only.")




