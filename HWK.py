try:
    age= int(input("Enter your age: "))

    if age < 0 or age > 120:
        raise ValueError("Age is not realistic.")

    if age % 2 == 0:
        print(age," is even.")
    else:
        print(age," is odd.")

except ValueError as x:
    print("Invalid input:", x)

except Exception as y:
    print("Unexpected error:", y)
else:
    print("No exceptions")
finally:
    print("This will execute no matter what!")