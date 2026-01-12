# for loops in python

for k in range(2,11,2): #start,stop and step
    print(k)

a = "Aanya"
for character in a:
    print(character)
    if character == "a":
        print("This Character is Speical")
Colours = [ "red","green","blue","pink"]
for color in Colours:
    print(color)
    if color=="pink":
     print("this is my favourite colour.")
    for i in color:
       print(i)

# while loops in python
i = 0 #incrementing while loop
while (i<5):
    print(i)
    i=i+1
    print(f"Done with the while loop {i}\n")

count = 10 #decrementing while loop
while(count>0):
    print(count)
    count=count-1
print("Happy New Year 2026!\n")

# break and continue statements
# break = loop ko chodkar nikal jao 
# continue =  uss iteration ko chodkar nikal jao
for i in range(11):
    if(i==10):
        break
    print("5 X ",i+1,"=",5*(i+1))
print("LOL! LOOP GOT BROKEN\n")

for i in range(12):
    if(i==10):
     print("LOL! A ITERATION JUST GOT SKIPPED")
     continue
    print("5 X ",i+1,"=",5*(i+1))
    
while True:
   print(i)
   i=i+1
   if(i%100==0):
    break




