
print("Aapka FunQuestions main Bhot Bhot Swagat Hai!")
print("Yeh Raha Aapka Pehla Sawaal Screen Par")
print("How many days are in the Leap Year?")
sum=0
Questions1=["Option 1:  364",
      "Option 2: 365",
      "Option 3: 366",
      "Option 4: 367"]
print(Questions1)
x = int(input("Enter the number: "))
if x==3:
    print("You WON Rs.10,000!")
    sum+=10000
else:
   print("You LOST Rs.10,000!")

print("What is the National Flower of India?")
Questions2=["Option 1:  Rose",
      "Option 2: Sunflower",
      "Option 3: Lotus",
      "Option 4: Jasmine"]
print(Questions2)
x1 = int(input("Enter the number: "))
if x1==3:
    print("You WON Rs.100,000!")
    sum+=100000
else:
   print("You LOST Rs.100,000!")


print(f"Congratulations! You won {sum} dhanrashi !", sum)
    