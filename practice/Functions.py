# functions in python
'''normally we write code to perform  task but when we need 
to perform specific tasks for n number of times we can use the function'''
# a=9
# b=8
# geometricmean=(a*b)/(a+b)
# c=8
# d=7
# geometricmean2=(c*d)/(c+d)
# print(geometricmean)
# print(geometricmean2)
def gmean(a,b): 
    '''gmean is a function name and a nad b are arguements or parameters'''
    mean=(a*b)/(a+b) 
    '''mean is a local variable'''
    print(mean)
def Greater(a,b):
    if(a>b):
     print("First nuber is greater.")
    else:
     print("Second number is greater or equal to.")
def islesser(a,b):
   pass
a=9
b=8
# if(a>b):
#     print("First nuber is greater.")
# else:
#     print("Second number is greater or equal to.")
Greater(a,b)
gmean(9,8)    
c=8
d=71
# if(c>d):
#     print("First nuber is greater.")
# else:
#     print("Second number is greater or equal to.")
Greater(c,d)
gmean(c,d)
''' basically gmean and Greater are short forms of
 the above functions which we can use repeatedly without 
 writing the whole code again and again for different values.
 These are like code words which perform specific tasks.'''

'''note.... 
1. function name should be unique.
2.Function should be defined before calling it.
3. Paremeters or arguements can be different while clling the function.
4.function can have more thsan on eparamenters.
5. Built in functions(min, max, range,print) do not need to be defined  while
user defined functions are deined by users using def 
{ def name parentheses parameters colon }keyword.
6. Any statements and other code within the function should be intended.
7. function can also return values using return keyword.'''










