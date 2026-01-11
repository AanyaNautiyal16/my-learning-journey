# using time module
import time
current_hour = int(input("Enter the current hour (0-23): "))
if current_hour<12:
    print("Good Morning Peopleee!!!")
elif current_hour<17:
    print("Good Afternoon Peopleeee!!!")
else:
    print("Good Evening Peopleee!!!!")
 #2nd Method 
import time
timestamp=time.strftime("%H:%M:%S")
print("Current time is: ",timestamp)
timestamp=time.strftime("%H")
print("Hours: ",timestamp)
timestamp=time.strftime("%M")
print("Minutes: ",timestamp)
timestamp=time.strftime("%S")
print("Seconds: ",timestamp)
