marks=int(input("Enter the marks out of 100:" ))
attendace=int(input("Enter the Attendace percentage: "))
if marks < 0 or marks > 100:
    print("Marks enetred are invalid!")
elif attendace < 0 or attendace > 100:
    print("Inavlid Attendace Percentage!")
#Bonus Condition
else:
    if marks >=45 and attendace >=90:
        if marks + 5 > 100:
             marks=100
        else:
            marks += 5
        print("Bonus Appied!")
#Result Clarification
if attendace < 75:
    print("Result: Failed due to isufficient Attendace!")
elif marks>= 90:
    print("Result: Passed, Excellent!")
elif marks>= 75:
    print("Result: Passed, Very Good!")
elif marks>= 50:
    print("Result: Passed, Good!")
else:
    print("Result: Failed!")

print("Evaluation Completed!")
             