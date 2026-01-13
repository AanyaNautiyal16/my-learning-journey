#function is used to separate the code
import numbers


def average(a=9,b=1):
    print("The average is: ", (a+b)/2)
average(4,2)   
'''deafault arguements can be provided. this way the function assumes
 the the default values if no values are provided while calling the function.'''
average(7) #value of a  
average(b=9) #value of b

def NAME(fname, mname="munnu" , lname="Nautiyal" ):
    print("Heyloo", fname,mname,lname)
NAME(fname="Aanya") #intendation is so much important . 
''' be cautious while writing the keywords or functions inside the function as before 
NAME wasnt printing because by default i have given space in front and made  it look like 
to python that the NAME is in the def keyword. SO be careful while intending.'''
NAME(fname="Aanya",mname="AANI")
'''we can change the order of arguements'''
NAME(mname="Munnu",fname="Nautiyal")


''' using tuples as arguements'''
def average(*numbers):
     print(type(numbers))
     sum=0
     for i in numbers:
         sum=sum+i
     print("Average is: ", sum/len(numbers))
average(2,3,6)


'''using dictionary as arguements'''
def name(**name):
 print(type(name))
 print("Hii Beutiful", name["fname"],name["lname"])
name(fname="Aanya", lname="Nautiyal")
name(lname="Nautiyal", fname="Aanya")

''' using tuples as arguements'''
def average(*numbers):
     print(type(numbers))
     sum=0
     for i in numbers:
         sum=sum+i
    #  print("Average is: ", sum/len(numbers))
     return sum/len(numbers)
c= average(5,6,7,1)
print(c)
''' we can also return values from functions using return keyword'''
''' we can store the returned value in a variable and use it later'''
''' return matlb vapas chale jao valye ko leke'''
