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

