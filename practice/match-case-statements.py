# switch case statements using match-case statements in python10+
# break statements are not used here as each case is automatically terminated after execution
# comparing a variable with all the patterns
# default case is automatically matched if other cases do not match
from unittest import case


x = int(input("Enter the number: "))
match x:
    case 0:
        print("The number is neither even nor odd!")
    case _ if x % 2 == 0:
        print(f"the entered number {x} is even!")
    case _ if x % 2 != 0:
        print(f"The entered number {x} is odd!")
        