
#class activity 1
fruit=["apple","banana","orange","berries"]
for list in fruit:
    print("the following lines will print each letter", list)
    for letters in list:
        print(letters)


#class activity 2
numbers = [9, 3, 2, 8, 4, 0, 4, 5, 9]
sum = 0
for val in numbers:
    sum =  sum + val
    print("The sum is", sum)      


#range function activity 3    
genre = ["action", "horror","thriller"]
for i in range(len(genre)):
    print("I like", genre[i])


#for loop with else class activity 4
digits = [5,9,1,12,20,21,3,]
for i in digits:
    print(i)
else:
    print("No items left.")


#class actvity 5    
x = 5
while x <=12:
   print(x)
   x = x + 5
print("done!")

    