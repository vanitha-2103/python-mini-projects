obtained = float(input("Enter your obtained total marks:"))
total = float(input("Enter your maximum total marks:"))

percentage = (obtained / total) * 100
print(f"Your Percentage is {round(percentage, 2)}%")

if percentage >= 90:
    print("Grade: A+")

elif percentage >= 80:
    print("Grade: A")

elif percentage >= 70:
    print("Grade: B")

elif percentage >= 60:
    print("Grade: C")

elif percentage >= 50:
    print("Grade: D")

else:
    print("Fail")
   