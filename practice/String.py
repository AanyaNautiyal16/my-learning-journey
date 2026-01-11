''' Practicing string slicing and operations on strings '''
name = "Aanya Nautiyal"
print(name[0:6])
fruit = "mango"
print(len(fruit))
print(fruit[:]) #without using len() fuction
print(fruit[0:3])
print(fruit[-1]) #negative slicing (including last character of the string)
print(fruit[-3:-1]) 
'''negative indexing starts from backwards of the string 
and positive indexing starts from the beginning of the string so here -3 and -2 are included while -1 is not included .''' 
print(fruit[-3:len(fruit)-1]) #python aumatically calculate that length and perform the function
 #quick quiz
nm="Harry"
print(nm[-4:-2])
''' String Methids in Python '''
# Strings are immutable
a = "aAnyaa !!! Aanyaa!!"
print(len(a)) #length
print(a.upper()) #uppercase
print(a.lower()) #lowercase
# removes the trailing part of the string and not the leading part i.e. "!" in this example
print(a.rstrip("!")) 
# replacing all the recurrences of aanyaa with aanya
print(a.replace("Aanyaa" , "Aanya"))
print(a.split(" "))#splits the string at the given character and returns a list
print(a.capitalize())#capitalizes the first letter of the string
print(a.count("!!"))
print(a.endswith("!!!"))
b="Aanyaa Nauti is 1 2 yal is a great human being\n"
print(b.center(30))
print(len(b))
print(len(b.center(30)))
#to check the value in between the string using slicing
print(b.endswith("Na",5,9))
# we can overwrite the variable in python but we cannot change the string , we can only create a new string
print(b.find("is")) #give the index of the first occurance of the given string
# INDEX METHOD
print(b.find("ish")) #returns -1 if not found! if we are sure then we can use find and if not use index
# print(b.index("ish")) #raise expception and ends the program if the string is not found returns substring not found error
x=" Aanya00 "
print(x.isalnum())
print(x.isalpha())
print(x.islower())
print(b.isprintable())
print(x.title())
print(x.isspace())
print(x.swapcase())
