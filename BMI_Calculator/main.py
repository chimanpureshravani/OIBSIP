
# ==========================================
# OASIS INFOBYTE - PYTHON PROGRAMMING
# TASK 2 - BMI CALCULATOR
# LEVEL - BEGINNER
# ==========================================


# Section 1: Display Project Heading

print("\n")
print("========================================")
print("          BMI CALCULATOR")
print("========================================")


# Section 2: Get User Input

try:

    # Accept weight from user
    weight = float(input("\nEnter your weight (in kg): "))

    # Accept height from user
    height = float(input("Enter your height (in meters): "))


    # Section 3: Validate User Input

    if weight <= 0 or height <= 0:

        print("\nError: Weight and Height must be greater than zero.")

    else:

        # Section 4: Calculate BMI

        bmi = weight / (height ** 2)

        # Round BMI to 2 decimal places
        bmi = round(bmi, 2)


        # Section 5: Determine BMI Category

        if bmi < 18.5:

            category = "Underweight"

        elif bmi < 25:

            category = "Normal Weight"

        elif bmi < 30:

            category = "Overweight"

        else:

            category = "Obese"


        # Section 6: Display Final Result

        print("\n")
        print("========================================")
        print("              BMI RESULT")
        print("========================================")

        print("Your Weight :", weight, "kg")
        print("Your Height :", height, "meters")
        print("Your BMI    :", bmi)
        print("Your Category:", category)

        print("========================================")

        print("\nThank you for using BMI Calculator!")


# Section 7: Handle Invalid Input

except ValueError:

    print("\nError: Please enter valid numeric values.")

except KeyboardInterrupt:

    print("\nProgram stopped by user.")


