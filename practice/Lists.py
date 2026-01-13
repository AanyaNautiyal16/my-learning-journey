# LISTS
''' lists are ordered collection od datatypes, seprated by
 commas and inclosed with square brackets
they are mutable and allow duplicate values'''
''' it can have multiple datatypes in a single list'''
''' in a list indexing starts with 0 till n-1 (n=number of elements in the list)
having unique index for each element in the list
 negative indexing is also allowed in the lists -1,-2,-3...-n
where -1 refers to last element of the list
 lists allow slicing operation to access a range of elements'''

l=[1,2,3]
print(l)
print(type(l))

marks=[20,0,79,100,78,68,56]
print(marks)
print(marks[0])
print(marks[1])
print(marks[2])

if "6" in marks : #no beacuse 6 is stored as a integer in the list and not as a strimg
    print("yes")
else:
    print("no")

print(marks)
print(marks[:])
print(marks[1:])
print(marks[1:len(marks)- -1])
print(marks[1:7:2])
print(marks[1:9:2])

lst=[i**i for i in range(10)if i%2==0]
print(lst)

# methods or Manipulating the lists
# append adds the element to the list at the end 
# sort helps in ascending order of the elements in the list
# reverse helps in reversing the order of the elements in the list
l = [1,2,3,0,4,8,2]
l.append(7)
print(l)
# l.sort(reverse=True)
# print(l)
l.sort()
print(l)
# l.reverse()
# print(l)
print(l.index(1))
print(l.count(1))
# m=l.copy()
# m[0]=0
# print(m)
l.insert(1,899)
m=[900,1000,1100,2000]
k=l+m
# l.extend(m)
print(k)