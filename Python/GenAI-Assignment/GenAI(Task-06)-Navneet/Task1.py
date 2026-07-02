try:
    numerator = float(input("Enter numerator: "))
    denominator = float(input("Enter denominator: "))

    result = numerator / denominator

except ValueError:
    print("Error: Please enter valid numbers.")

except ZeroDivisionError:
    print("Error: Denominator cannot be zero.")

else:
    print("Result:", result)

finally:
    print("Operation Complete")