# tuples are ordered collection of data item which are immutable
# items are seperated by commas and are enclesed within () brackets.
tup1=(1 ,5 ,6)
print(type(tup1),tup1)
tup2=(1)
print(type(tup2),tup2)
'''if we don't put comma in a tuple with single element it just gives a type int'''
'''we have to put a comma after the element if a tuple has only one element 
in order to consider the type tuple by the python'''
tup3=(1,)
print(type(tup3),tup3)
'''elemets cannot be changed by using also the indexing method as used in list
but if you want to make the items permanent or constant so you shouldmuse tuple
because of its immutable property'''
# accesing the tuple elements
print(tup1[0])
print(tup1[1])
print(tup1[2])
# print(tup1[11]) #gives error as elements are from 0-2 only
'''index was out of range'''
print(len(tup1))

tup=(1,2,3,4,5,6,7,8,0)
print(len(tup))
if 9 in tup:
    print("Yes!")
else:
    print("No!")

# slicing returns a new tuple
tup1=tup[0:10]
print(tup1)

# operations on tuples
'''tuple cant be maniplated directly , you have to copy that tuple
 and change it into list and then convert it into a tuple'''
# what if i want to add something in a tuple?.....change it into a list
countries=("India","Nepal","Bhutan","china","pakistan","myanmar","SriLanka")
temp=list(countries)
temp.append("Bangladesh")
print(temp)
temp[2]="Bhutan"
temp.pop(6)
print(temp)
countries=tuple(temp)
print(countries)

c1=(1,2,3,4)
c2=(5,6,7,8)
numbers=c1+c2
print(numbers)

c=(1,2,1,1,1,2,3,0,0)
rep=c.count(1)
print("number of ones in tuple is: ",rep)

# index method gives first occuranes of the given element from the tuple.
c=(1,2,1,1,1,2,3,0,0)
rep=c.index(2)
print("first occurance of 2 in tuple is: ",rep)
temp=list(c)
temp[1]=21
c=tuple(temp)
rep=c.index(2)
print("first occurance of 2 in tuple is: ",rep)
c1=(1,2,1,1,1,2,3,0,0)
rep1=c1.index(1, 4, 9) #1 find,5 to 9 sliced
print("first occurance of 1 in tuple is: ",rep1)


